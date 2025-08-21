#!/usr/bin/env python3
"""
Enhanced Aqara Token Generator for FP2 Node-RED Integration
Automatically generates and refreshes Aqara API tokens using username/password

Usage:
  python3 fp2_token_generator.py <username> <password> <area>
  
Areas: EU, US, CN, RU, KR, JP, AF, AU, ME, HMT, OTHER

This script is designed to work with Node-RED exec nodes and provides
structured output for easy parsing.
"""

import sys
import os
import json
import subprocess
import tempfile
import time
from pathlib import Path

def install_requirements():
    """Install required Python packages if not available"""
    required_packages = ['pycryptodome', 'requests', 'requests-toolbelt']
    
    for package in required_packages:
        try:
            __import__(package.replace('-', '_').replace('pycryptodome', 'Crypto'))
        except ImportError:
            print(f"Installing {package}...", file=sys.stderr)
            try:
                subprocess.check_call([
                    sys.executable, '-m', 'pip', 'install', '-q', package
                ])
            except subprocess.CalledProcessError as e:
                print(f"Failed to install {package}: {e}", file=sys.stderr)
                return False
    return True

def download_official_script():
    """Download the official Aqara token generator script"""
    script_url = "https://raw.githubusercontent.com/sdavides/AqaraPOST-Homeassistant/main/generatejson/AqaraPOST-tokenGenerator.py"
    script_path = "/tmp/AqaraPOST-tokenGenerator.py"
    
    try:
        import requests
        response = requests.get(script_url, timeout=30)
        response.raise_for_status()
        
        with open(script_path, 'w') as f:
            f.write(response.text)
        
        os.chmod(script_path, 0o755)
        return script_path
    except Exception as e:
        # Fallback to wget if requests fails
        try:
            subprocess.check_call([
                'wget', '-q', script_url, '-O', script_path
            ])
            os.chmod(script_path, 0o755)
            return script_path
        except subprocess.CalledProcessError:
            print(f"Failed to download token generator script: {e}", file=sys.stderr)
            return None

def generate_tokens(username, password, area):
    """Generate Aqara tokens using the official script"""
    
    # Install requirements
    if not install_requirements():
        return {"success": False, "error": "Failed to install required packages"}
    
    # Download official script
    script_path = download_official_script()
    if not script_path:
        return {"success": False, "error": "Failed to download token generator script"}
    
    try:
        # Run the official token generator script
        process = subprocess.Popen(
            [sys.executable, script_path],
            stdin=subprocess.PIPE,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            text=True,
            cwd='/tmp'
        )
        
        # Provide input automatically (username, password, area)
        input_data = f"{username}\n{password}\n{area}\n"
        
        try:
            stdout, stderr = process.communicate(input=input_data, timeout=60)
        except subprocess.TimeoutExpired:
            process.kill()
            return {"success": False, "error": "Token generation timed out"}
        
        if process.returncode == 0:
            return {
                "success": True, 
                "output": stdout,
                "error": None,
                "stderr": stderr
            }
        else:
            return {
                "success": False,
                "output": stdout,
                "error": f"Token generation failed (exit code {process.returncode})",
                "stderr": stderr
            }
            
    except Exception as e:
        return {"success": False, "error": f"Exception during token generation: {str(e)}"}
    
    finally:
        # Cleanup
        if os.path.exists(script_path):
            try:
                os.remove(script_path)
            except:
                pass

def parse_token_output(output):
    """Parse the token generator output to extract structured data"""
    lines = output.split('\n')
    
    result = {
        'token': '',
        'appid': '',
        'server': '',
        'userid': '',
        'devices': []
    }
    
    # Parse token information
    for line in lines:
        line = line.strip()
        if 'Token:' in line:
            result['token'] = line.split('Token:', 1)[1].strip()
        elif 'AppID:' in line:
            result['appid'] = line.split('AppID:', 1)[1].strip()
        elif 'Server:' in line:
            result['server'] = line.split('Server:', 1)[1].strip()
        elif 'UserID:' in line:
            result['userid'] = line.split('UserID:', 1)[1].strip()
    
    # Try to parse device information from JSON output
    json_start = output.find('{')
    if json_start != -1:
        json_end = output.rfind('}') + 1
        if json_end > json_start:
            try:
                json_data = json.loads(output[json_start:json_end])
                if 'result' in json_data and 'data' in json_data['result']:
                    result['devices'] = json_data['result']['data']
            except json.JSONDecodeError:
                pass
    
    return result

def main():
    if len(sys.argv) != 4:
        print("Usage: python3 fp2_token_generator.py <username> <password> <area>")
        print("Areas: EU, US, CN, RU, KR, JP, AF, AU, ME, HMT, OTHER")
        sys.exit(1)
    
    username = sys.argv[1]
    password = sys.argv[2]
    area = sys.argv[3].upper()
    
    # Validate area
    valid_areas = ["CN", "EU", "RU", "KR", "JP", "AF", "USA", "OTHER", "US", "HMT", "AU", "ME"]
    if area not in valid_areas:
        print(f"Invalid area '{area}'. Valid areas: {', '.join(valid_areas)}", file=sys.stderr)
        sys.exit(1)
    
    print(f"Starting token generation for {username} in {area} region...")
    
    # Generate tokens
    result = generate_tokens(username, password, area)
    
    if result["success"]:
        # Parse the output for structured data
        parsed = parse_token_output(result["output"])
        
        if parsed['token'] and parsed['appid'] and parsed['server']:
            # Output structured results
            print("#### Token Generation Successful ####")
            print(f"Token:{parsed['token']}")
            print(f"AppID:{parsed['appid']}")
            print(f"Server:{parsed['server']}")
            print(f"UserID:{parsed['userid']}")
            print(f"Timestamp:{int(time.time())}")
            
            if parsed['devices']:
                print("#### Available Devices ####")
                for i, device in enumerate(parsed['devices']):
                    if isinstance(device, dict) and 'subjectId' in device:
                        print(f"Device{i+1}:{device['subjectId']}")
            
            print("#### End Token Generation ####")
            
        else:
            print("Failed to parse token information from output", file=sys.stderr)
            print("Raw output:", file=sys.stderr)
            print(result["output"], file=sys.stderr)
            sys.exit(1)
    else:
        print(f"Token generation failed: {result['error']}", file=sys.stderr)
        if result.get('stderr'):
            print("Error details:", file=sys.stderr)
            print(result['stderr'], file=sys.stderr)
        if result.get('output'):
            print("Output:", file=sys.stderr) 
            print(result['output'], file=sys.stderr)
        sys.exit(1)

if __name__ == "__main__":
    main()
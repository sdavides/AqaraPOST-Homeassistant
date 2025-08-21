# FP2 Auto-Token Refresh Setup Guide

This guide helps you set up your Aqara FP2 presence sensor with Home Assistant using **Method 2** (manual Node-RED import) while maintaining automatic token refresh functionality like **Method 1**.

## 🎯 What This Solves

- ✅ **Auto-refresh tokens** using username/password (no manual token updates)
- ✅ **Works with FP2** (not just G3 camera)
- ✅ **No add-on required** (pure Node-RED solution)  
- ✅ **Compatible with existing FP2 flow**

## 📋 Prerequisites

1. **Home Assistant** with Node-RED installed
2. **Node-RED Companion** (install from HACS)
3. **Aqara account credentials** (username/password)
4. **Your FP2 device ID** (lumi1.xxxxxxxxx format)

## 🛠️ Setup Steps

### Step 1: Import the Token Management Flow

1. **Copy the token refresh flow**:
   - Import `Aqara_FP2_TokenRefresh_nodered.json` into Node-RED
   - This creates a new tab called "FP2 Token Management"

2. **Configure your credentials**:
   - Open the **"Aqara Credentials"** change node
   - Replace the placeholder values:
     ```
     aqara_username: your_email@example.com
     aqara_password: your_password  
     aqara_area: EU (or US, CN, etc.)
     aqara_subjectId: lumi1.XXXXXXXXXXXX (your FP2 device ID)
     aqara_timezone: en-UK (or it-IT, es-ES, etc.)
     ```

### Step 2: Import Your FP2 Flow

1. **Import the FP2 flow**:
   - Import the original `Aqara_FP2_nodered.json` file
   - The FP2 flow will automatically use the global variables set by the token management system

### Step 3: Deploy and Test

1. **Deploy your flows** (both tabs)

2. **Generate initial tokens**:
   - Click the **"Manual Refresh"** inject node
   - Watch the debug output for success/error messages

3. **Verify tokens were created**:
   - Go to **Context Data** (right panel) → **Global**
   - Check that these variables exist:
     - `token`
     - `appid` 
     - `aqara_url`
     - `subjectId`
     - `userid`
     - `country`

## 🔄 How It Works

### Automatic Token Refresh
- **Every 6 hours**: System checks if tokens are older than 23 hours
- **Auto-refresh**: If needed, generates new tokens using your username/password
- **Global storage**: Stores tokens in global variables for your FP2 flow to use

### Manual Control  
- **Manual Refresh**: Click anytime to force immediate token generation
- **Startup Refresh**: Automatically checks tokens when Node-RED starts

### Status Monitoring
- **Home Assistant Entity**: Creates "FP2 Token Status" sensor showing connection state
- **Debug Output**: View detailed token information and errors
- **Visual Status**: Node colors indicate token health (green=good, red=error, yellow=refreshing)

## 🔍 Finding Your FP2 Device ID

If you don't know your FP2's device ID (lumi1.xxxxxxxxx):

1. **Run the token generator once**:
   - Use the manual refresh with placeholder values
   - Look in the debug output for "Available Devices"
   - Find your FP2 device ID in the list

2. **Alternative method**:
   - Use the original Python script manually:
     ```bash
     python3 fp2_token_generator.py your_email@example.com your_password EU
     ```
   - Look for device list in output

## 🏠 Home Assistant Integration

The token management system creates a Home Assistant sensor:

- **Entity ID**: `sensor.fp2_token_status`
- **States**: "Connected" (tokens valid) or "Error" (refresh needed)
- **Attributes**:
  - `last_refresh`: When tokens were last updated
  - `server`: Your Aqara server URL
  - `subject_id`: Your FP2 device ID
  - `token_preview`: First 10 characters of current token

## 🚨 Troubleshooting

### Token Generation Fails

1. **Check credentials**:
   - Verify username/password are correct
   - Ensure area code is valid (EU, US, CN, etc.)

2. **Check debug output**:
   - Look for specific error messages
   - Verify Python dependencies are installed

3. **Manual test**:
   ```bash
   python3 /home/erib/project/AqaraPOST-Homeassistant/fp2_token_generator.py your_email your_password EU
   ```

### FP2 Flow Not Working

1. **Verify global variables**:
   - Check Context Data → Global for required variables
   - Ensure `subjectId` matches your FP2 device

2. **Check token age**:
   - Look at `token_last_refresh` timestamp
   - Try manual refresh if tokens are old

### Python Dependencies

If you get import errors:
```bash
python3 -m pip install pycryptodome requests requests-toolbelt
```

## 📁 Files Created

- `Aqara_FP2_TokenRefresh_nodered.json` - Token management flow
- `fp2_token_generator.py` - Enhanced Python token generator  
- `FP2_SETUP_INSTRUCTIONS.md` - This guide
- `fp2_config_template.json` - Configuration examples

## 🔧 Advanced Configuration

### Custom Refresh Interval

To change the auto-refresh interval:
1. Edit the "Auto Refresh" inject node
2. Change the repeat interval (default: 21600 seconds = 6 hours)

### Multiple Devices

To support multiple Aqara devices:
1. Add additional `subjectId` variables in the credentials node
2. Modify the FP2 flow to use the correct device ID

## 🆘 Support

If you encounter issues:

1. **Check the debug output** for detailed error messages
2. **Verify your credentials** and device ID are correct
3. **Test the Python script manually** to isolate issues
4. **Check Home Assistant logs** for Node-RED errors

## 🎉 Success Indicators

You'll know everything is working when:

- ✅ "FP2 Token Status" shows "Connected" in Home Assistant
- ✅ Debug output shows successful token generation  
- ✅ Your FP2 presence sensor data appears in Home Assistant
- ✅ Tokens refresh automatically without manual intervention

---

**Enjoy your automated FP2 presence sensor with self-refreshing tokens!** 🚀
# Changelog - FP2 Fork

## Version fp2-1.0 (2024-08-21)

### 🎉 New Features
- **FP2 Support**: Add-on now defaults to FP2 Presence Sensor instead of G3 Camera
- **Device Type Selection**: Choose between FP2 and G3 in configuration
- **Swedish Locale**: Added sv-SE timezone support
- **Smart Token Replacement**: Custom logic for FP2 flow token injection

### 🔄 Changes  
- **Default Device**: Changed from G3 Camera to FP2 Presence Sensor
- **Add-on Name**: Updated to `AqaraPost_FP2_[Node-RED]`
- **Configuration**: Added `deviceType` option (FP2/G3)
- **Default Timezone**: Changed from it-IT to sv-SE
- **Flow Download**: Automatically downloads correct flow based on device type

### 🛠️ Technical Updates
- Modified `/addon-AqaraPost/config.yaml`:
  - Added `deviceType: FP2` option
  - Updated default timezone to `sv-SE`
  - Changed addon name and description
  
- Updated `/addon-AqaraPost/rootfs/etc/s6-overlay/s6-rc.d/init-nodered/run`:
  - Added device type detection
  - Smart flow selection (FP2 vs G3)
  - Custom token replacement for FP2 flows
  - Improved error handling

- Enhanced documentation:
  - Updated README with FP2 focus
  - Added configuration instructions
  - Clarified device support

### 📋 Configuration Options

```yaml
options:
  usernameAqara: your_email@example.com
  passwordAqara: your_password
  serverAqara: EU
  lumi1Aqara: lumi1.your_device_id
  timezoneAqara: sv-SE
  deviceType: FP2  # New option: FP2 or G3
```

### 🎯 How It Works

1. **FP2 Mode (Default)**:
   - Downloads `Aqara_FP2_nodered.json`
   - Uses custom token replacement
   - Optimized for presence sensor functionality

2. **G3 Mode (Legacy)**:
   - Downloads `Aqara_G3_nodered.json`
   - Uses original token generation script
   - Full camera functionality

### 🚀 Benefits

- ✅ **One-click FP2 setup** with username/password
- ✅ **Automatic token refresh** (same as G3 version)
- ✅ **Swedish locale support**
- ✅ **Backward compatible** with G3 cameras
- ✅ **Method 1 simplicity** for FP2 users

### 📦 Installation

1. Add this repository to Home Assistant:
   ```
   https://github.com/your-username/AqaraPOST-Homeassistant
   ```

2. Install "AqaraPost_FP2_[Node-RED]" add-on

3. Configure with your Aqara credentials and FP2 device ID

4. Start the add-on - it automatically:
   - Installs Python and dependencies
   - Generates tokens from your credentials  
   - Downloads and configures FP2 flow
   - Sets up Node-RED with working FP2 integration

### 🔧 Migration from Original

If migrating from the original G3 add-on:

1. **Keep G3 functionality**: Set `deviceType: G3` in configuration
2. **Switch to FP2**: Set `deviceType: FP2` and update `lumi1Aqara` with FP2 device ID

### 🐛 Known Issues

- FP2 flow must exist in the original repository
- Token replacement assumes specific placeholder format in FP2 flow
- Swedish locale may need validation with Aqara API

### 🔮 Future Plans

- Auto-detection of device type based on device ID
- Support for multiple devices in single add-on
- Enhanced error reporting and diagnostics
- Web UI for token management
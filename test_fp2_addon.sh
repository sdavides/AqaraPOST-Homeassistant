#!/bin/bash

# Test script for FP2 add-on modifications
# This script validates the changes made to support FP2

echo "🧪 Testing FP2 Add-on Modifications..."
echo "=================================="

# Test 1: Check config.yaml has FP2 support
echo -n "✓ Testing config.yaml FP2 support... "
if grep -q "deviceType.*FP2" addon-AqaraPost/config.yaml && grep -q "sv-SE" addon-AqaraPost/config.yaml; then
    echo "PASS"
else
    echo "FAIL"
fi

# Test 2: Check init script has FP2 logic
echo -n "✓ Testing init script FP2 logic... "
if grep -q "DEVICE_TYPE.*FP2" addon-AqaraPost/rootfs/etc/s6-overlay/s6-rc.d/init-nodered/run && grep -q "Aqara_FP2_nodered.json" addon-AqaraPost/rootfs/etc/s6-overlay/s6-rc.d/init-nodered/run; then
    echo "PASS"
else
    echo "FAIL"
fi

# Test 3: Check README mentions FP2
echo -n "✓ Testing README FP2 documentation... "
if grep -q "FP2 Presence Sensor" addon-AqaraPost/README.md; then
    echo "PASS"
else
    echo "FAIL"
fi

# Test 4: Validate script syntax
echo -n "✓ Testing bash script syntax... "
if bash -n addon-AqaraPost/rootfs/etc/s6-overlay/s6-rc.d/init-nodered/run; then
    echo "PASS"
else
    echo "FAIL"
fi

# Test 5: Check required files exist
echo "✓ Checking file structure:"
for file in \
    "addon-AqaraPost/config.yaml" \
    "addon-AqaraPost/README.md" \
    "addon-AqaraPost/rootfs/etc/s6-overlay/s6-rc.d/init-nodered/run" \
    "Aqara_FP2_nodered.json" \
    "CHANGELOG_FP2.md"; do
    if [ -f "$file" ]; then
        echo "  ✓ $file exists"
    else
        echo "  ✗ $file missing"
    fi
done

echo ""
echo "🎯 Summary of Changes:"
echo "- Add-on name: AqaraPost_FP2_[Node-RED]"
echo "- Default device: FP2 Presence Sensor"
echo "- Default timezone: sv-SE (Swedish)"
echo "- Device type selection: FP2 or G3"
echo "- Smart flow download based on device type"
echo "- Custom token replacement for FP2"

echo ""
echo "📋 Next Steps:"
echo "1. Push changes to your GitHub fork"
echo "2. Add the repository to Home Assistant"
echo "3. Install the modified add-on"
echo "4. Configure with your FP2 credentials"
echo "5. Test the FP2 integration"

echo ""
echo "🚀 Ready to use Method 1 with your FP2!"
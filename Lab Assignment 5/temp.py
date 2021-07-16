import os
os.system('cmd /c "reg add HKEY_LOCAL_MACHINE\\SOFTWARE\\Microsoft\\WindowsUpdate\\UX\\Settings /v FlightSettingsMaxPauseDays /t REG_DWORD /d 365" /f')
os.system('cmd /c "reg add HKEY_LOCAL_MACHINE\\SOFTWARE\\Microsoft\\WindowsUpdate\\UX\\Settings /v PauseFeatureUpdatesEndTime /t REG_SZ /d 2050-01-01T10:38:56Z /f"')
os.system('cmd /c "reg add HKEY_LOCAL_MACHINE\\SOFTWARE\\Microsoft\\WindowsUpdate\\UX\\Settings /v PauseQualityUpdatesEndTime /t REG_SZ /d 2050-01-01T10:38:56Z /f"')
os.system('cmd /c "reg add HKEY_LOCAL_MACHINE\\SOFTWARE\\Microsoft\\WindowsUpdate\\UX\\Settings /v PauseUpdatesExpiryTime /t REG_SZ /d 2050-01-01T10:38:56Z /f"')

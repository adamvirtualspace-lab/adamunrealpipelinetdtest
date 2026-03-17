@echo off
setlocal

:: Get the directory of the batch file
set "currentDir=%~dp0"

echo Cleaning Unreal Engine project folders in: %currentDir%
echo.

:: Delete full folders
for %%F in (Binaries DerivedDataCache Intermediate) do (
    if exist "%currentDir%%%F" (
        echo Deleting folder: %%F
        rmdir /s /q "%currentDir%%%F"
    ) else (
        echo Folder not found: %%F
    )
)

:: Clean Build folder contents (keep folder itself)
set "buildDir=%currentDir%Build"
if exist "%buildDir%" (
    echo Cleaning contents of Build folder...
    del /f /q "%buildDir%\*" 2>nul
    for /d %%D in ("%buildDir%\*") do (
        rmdir /s /q "%%D"
    )
) else (
    echo Build folder not found.
)

:: Handle Saved folder
set "savedDir=%currentDir%Saved"
if exist "%savedDir%" (
    echo.
    echo Cleaning Saved folder, preserving Config...
    
    for /d %%D in ("%savedDir%\*") do (
        if /i not "%%~nxD"=="Config" (
            echo Deleting folder: %%~nxD
            rmdir /s /q "%%D"
        )
    )
    for %%F in ("%savedDir%\*") do (
        if not exist "%%F\" (
            echo Deleting file: %%~nxF
            del /f /q "%%F"
        )
    )
) else (
    echo Saved folder not found.
)

echo.
echo Done!
pause

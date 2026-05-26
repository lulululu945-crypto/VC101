@echo off
REM Windows Batch Script to Download and Setup Background Video
REM 視頻下載和設置助手

setlocal enabledelayedexpansion

echo.
echo ========================================
echo 🎬 Background Video Setup Assistant
echo ========================================
echo.

REM Check if Python is installed
python --version >nul 2>&1
if errorlevel 1 (
    echo ❌ Python is not installed or not in PATH
    echo Please install Python from https://www.python.org/
    pause
    exit /b 1
)

echo ✅ Python found

REM Check if yt-dlp is installed
python -m pip show yt-dlp >nul 2>&1
if errorlevel 1 (
    echo Installing yt-dlp...
    python -m pip install yt-dlp -q
    if errorlevel 1 (
        echo ❌ Failed to install yt-dlp
        pause
        exit /b 1
    )
    echo ✅ yt-dlp installed
) else (
    echo ✅ yt-dlp found
)

REM Check if FFmpeg is installed
ffmpeg -version >nul 2>&1
if errorlevel 1 (
    echo.
    echo ⚠️  FFmpeg is not installed!
    echo Please download from: https://ffmpeg.org/download.html
    echo Or install via: choco install ffmpeg
    echo.
    pause
    exit /b 1
)
echo ✅ FFmpeg found

REM Create output directory
if not exist "assets\video" (
    mkdir assets\video
    echo 📁 Created assets\video directory
)

REM Prompt for YouTube URL
set /p youtube_url="🔗 Enter YouTube URL: "

if "%youtube_url%"=="" (
    echo ❌ No URL provided
    pause
    exit /b 1
)

REM Download video
echo.
echo 📥 Downloading video...
python -m yt_dlp -f "best[ext=mp4]" -o "temp_video.mp4" "%youtube_url%"

if errorlevel 1 (
    echo ❌ Download failed
    pause
    exit /b 1
)

echo ✅ Download complete

REM Optimize video
echo.
echo ⚙️  Optimizing video for web...
ffmpeg -i temp_video.mp4 -vf scale=1920:1080:force_original_aspect_ratio=decrease -c:v libx264 -preset medium -crf 23 -c:a aac -b:a 128k -y assets\video\bg-video.mp4

if errorlevel 1 (
    echo ❌ Optimization failed
    pause
    exit /b 1
)

echo ✅ Video optimized

REM Cleanup
del temp_video.mp4

echo.
echo ========================================
echo ✅ SUCCESS! Video is ready!
echo ========================================
echo.
echo 📁 Video saved to: assets\video\bg-video.mp4
echo 🚀 You can now use it in your website!
echo.

pause

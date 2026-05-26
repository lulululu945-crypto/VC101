#!/usr/bin/env python3
"""
YouTube Video Downloader & Optimizer for Background Video
自動下載和優化 YouTube 視頻作為網站背景

Usage:
    python download_bg_video.py
"""

import os
import subprocess
import sys

def check_requirements():
    """Check if required tools are installed"""
    print("🔍 Checking required tools...")
    
    try:
        import yt_dlp
        print("✅ yt-dlp is installed")
    except ImportError:
        print("❌ yt-dlp not found. Installing...")
        subprocess.run([sys.executable, "-m", "pip", "install", "yt-dlp"], check=True)
    
    # Check for ffmpeg
    try:
        subprocess.run(["ffmpeg", "-version"], capture_output=True, check=True)
        print("✅ FFmpeg is installed")
    except (FileNotFoundError, subprocess.CalledProcessError):
        print("⚠️  FFmpeg is not installed!")
        print("   Please download from: https://ffmpeg.org/download.html")
        print("   Or install via: brew install ffmpeg (Mac) / choco install ffmpeg (Windows)")
        return False
    
    return True

def download_video(youtube_url):
    """Download video from YouTube"""
    print(f"\n📥 Downloading video from: {youtube_url}")
    
    import yt_dlp
    
    ydl_opts = {
        'format': 'best[ext=mp4]',
        'outtmpl': 'temp_video.mp4',
        'quiet': False,
        'no_warnings': False,
    }
    
    try:
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            info = ydl.extract_info(youtube_url, download=True)
            print(f"✅ Downloaded: {info['title']}")
            return True
    except Exception as e:
        print(f"❌ Download failed: {e}")
        return False

def optimize_video():
    """Optimize video using FFmpeg"""
    print("\n⚙️  Optimizing video for web...")
    
    input_file = "temp_video.mp4"
    output_file = os.path.join("assets", "video", "bg-video.mp4")
    
    # Ensure output directory exists
    os.makedirs(os.path.dirname(output_file), exist_ok=True)
    
    # FFmpeg command for optimization
    cmd = [
        "ffmpeg",
        "-i", input_file,
        "-vf", "scale=1920:1080:force_original_aspect_ratio=decrease",
        "-c:v", "libx264",
        "-preset", "medium",
        "-crf", "23",
        "-c:a", "aac",
        "-b:a", "128k",
        "-y",  # Overwrite output file
        output_file
    ]
    
    try:
        print(f"   Converting to: {output_file}")
        subprocess.run(cmd, check=True)
        print(f"✅ Video optimized: {output_file}")
        
        # Get file size
        size_mb = os.path.getsize(output_file) / (1024 * 1024)
        print(f"   File size: {size_mb:.2f} MB")
        
        return True
    except subprocess.CalledProcessError as e:
        print(f"❌ Optimization failed: {e}")
        return False

def create_webm_version():
    """Create WebM version for better compatibility"""
    print("\n⚙️  Creating WebM version for better compatibility...")
    
    input_file = os.path.join("assets", "video", "bg-video.mp4")
    output_file = os.path.join("assets", "video", "bg-video.webm")
    
    cmd = [
        "ffmpeg",
        "-i", input_file,
        "-c:v", "libvpx-vp9",
        "-b:v", "1M",
        "-c:a", "libopus",
        "-b:a", "128k",
        "-y",
        output_file
    ]
    
    try:
        subprocess.run(cmd, check=True)
        print(f"✅ WebM version created: {output_file}")
        
        size_mb = os.path.getsize(output_file) / (1024 * 1024)
        print(f"   File size: {size_mb:.2f} MB")
        
        return True
    except subprocess.CalledProcessError as e:
        print(f"⚠️  WebM creation failed (this is optional): {e}")
        return False

def cleanup():
    """Remove temporary files"""
    print("\n🧹 Cleaning up temporary files...")
    if os.path.exists("temp_video.mp4"):
        os.remove("temp_video.mp4")
        print("✅ Temporary files removed")

def main():
    print("=" * 60)
    print("🎬 YouTube Background Video Downloader & Optimizer")
    print("=" * 60)
    
    # Check requirements
    if not check_requirements():
        print("\n⚠️  Please install FFmpeg and try again.")
        sys.exit(1)
    
    # Get YouTube URL
    youtube_url = input("\n🔗 Enter YouTube URL (e.g., https://youtu.be/VIDEO_ID): ").strip()
    
    if not youtube_url:
        print("❌ No URL provided")
        sys.exit(1)
    
    # Download
    if not download_video(youtube_url):
        sys.exit(1)
    
    # Optimize
    if not optimize_video():
        sys.exit(1)
    
    # Create WebM version
    create_webm_version()
    
    # Cleanup
    cleanup()
    
    print("\n" + "=" * 60)
    print("✅ SUCCESS! Your video is ready!")
    print("=" * 60)
    print(f"\n📁 Video files saved to: assets/video/")
    print(f"📝 Update your HTML to use: <source src='assets/video/bg-video.mp4'>")
    print(f"\n🚀 You can now use the video in your website!")
    print("\n" + "=" * 60)

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\n\n⛔ Cancelled by user")
        sys.exit(0)
    except Exception as e:
        print(f"\n❌ Error: {e}")
        sys.exit(1)

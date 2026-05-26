# 🎬 視頻背景網站設置指南

## 📋 項目概述
你現在有一個專業的全屏視頻背景網站模板，具備：
- ✅ 自動播放、靜音、循環的視頻背景
- ✅ 響應式設計（支持所有設備）
- ✅ 優化的字體排版（使用Inter和Noto Sans TC）
- ✅ 高對比度設計（確保文字清晰可讀）
- ✅ 專業的動畫和交互效果

---

## 📹 第一步：準備視頻文件

### 選項 1：下載 YouTube 視頻（推薦）
1. **使用 yt-dlp 或 youtube-dl**
   ```bash
   # 安裝工具
   pip install yt-dlp

   # 下載視頻（MP4格式）
   yt-dlp -f "best[ext=mp4]" "https://youtu.be/i-gmUH_d_8w" -o "bg-video.mp4"
   ```

2. **或使用在線工具**
   - 訪問: https://www.4kdownload.com/
   - 訪問: https://y2mate.com/
   - 訪問: https://savefrom.net/

### 選項 2：使用已有的視頻文件
如果你已有視頻文件，只需將其放在正確的位置即可。

---

## 📁 第二步：檔案組織

將視頻文件放在以下位置：

```
VC101/
├── assets/
│   └── video/
│       ├── bg-video.mp4        (必需 - 主視頻文件)
│       └── bg-video.webm       (可選 - 備用格式)
├── index_video_bg.html         (新的視頻背景版本)
├── index.html                  (原始版本 - 保留備份)
└── ...其他文件
```

---

## 🎯 第三步：視頻優化（重要！）

為了最佳性能，建議優化視頻：

### 使用 FFmpeg 優化視頻
```bash
# 1. 安裝 FFmpeg (Windows)
# 下載: https://ffmpeg.org/download.html

# 2. 優化MP4格式（減小文件大小）
ffmpeg -i original-video.mp4 -c:v libx264 -preset medium -crf 23 -c:a aac -b:a 128k bg-video.mp4

# 3. 如果需要 WebM 格式（更好的壓縮）
ffmpeg -i original-video.mp4 -c:v libvpx-vp9 -b:v 1M -c:a libopus -b:a 128k bg-video.webm

# 4. 調整視頻分辨率（建議1920x1080）
ffmpeg -i original-video.mp4 -vf scale=1920:1080 -c:v libx264 -preset medium -crf 23 bg-video.mp4
```

### 視頻規格建議
- **分辨率**: 1920×1080px (Full HD) 或 2560×1440px (2K)
- **幀率**: 24-30fps
- **文件大小**: 5-30MB（網頁使用）
- **格式**: MP4（主要） + WebM（備用）
- **長度**: 10-30秒（會自動循環）

---

## 🚀 第四步：使用新的網站版本

### 替換主文件
```bash
# 方法1：重命名
ren index.html index_old.html
ren index_video_bg.html index.html

# 方法2：複製內容
# 將 index_video_bg.html 的內容複製到 index.html
```

或者直接在瀏覽器中打開：
- `http://localhost/VC101/index_video_bg.html` 來測試

---

## 🎨 自定義選項

### 1. 調整視頻透明度
在 CSS 中找到：
```css
.video-bg-container video {
    opacity: 0.85;  /* 改變這個值 (0-1) */
}
```

### 2. 調整覆蓋層亮度
```css
.video-overlay {
    background: linear-gradient(
        135deg, 
        rgba(15, 23, 42, 0.65) 0%,  /* 調整數值改變亮度 */
        rgba(31, 41, 55, 0.5) 50%,
        rgba(15, 23, 42, 0.65) 100%
    );
}
```

### 3. 更改文字顏色
搜索下列類並修改：
- `.text-white` → 改為其他顏色
- `.text-cyan-300` → 改為其他強調色
- `.text-white/90` → 改為其他透明度

### 4. 調整視頻亮度和對比度
```css
.video-bg-container video {
    filter: brightness(0.75) contrast(1.1);  /* 調整這些值 */
}
```

---

## ✅ 測試清單

- [ ] 視頻文件已放在 `assets/video/` 文件夾中
- [ ] 視頻自動播放且循環
- [ ] 視頻在所有設備上全屏顯示
- [ ] 文字在視頻背景上清晰可見
- [ ] 所有按鈕和鏈接都正常工作
- [ ] 頁面在手機上響應式顯示
- [ ] 視頻文件大小合理（不超過50MB）

---

## 🔧 故障排除

### 視頻不播放
1. 檢查文件路徑是否正確
2. 確保文件名為 `bg-video.mp4` 或 `bg-video.webm`
3. 檢查瀏覽器是否支持該視頻格式
4. 試試使用另一種視頻格式（MP4 或 WebM）

### 文字不清晰
1. 增加視頻的亮度過濾器
2. 增加覆蓋層的不透明度（改大rgba中的數值）
3. 使用深色的文本陰影
4. 改用對比度更高的視頻

### 性能緩慢
1. 減小視頻文件大小
2. 降低視頻分辨率
3. 使用 WebM 格式而非 MP4
4. 在服務器上啟用 gzip 壓縮

---

## 📱 響應式設計特性

網站已優化以支持：
- 📱 手機 (320px 及以上)
- 📱 平板 (768px 及以上)
- 💻 桌面 (1024px 及以上)
- 🖥️ 大屏幕 (1920px 及以上)

視頻背景在所有設備上自動適應！

---

## 🎯 最終步驟

1. ✅ 準備你的視頻文件
2. ✅ 放在 `assets/video/` 文件夾中
3. ✅ 打開 `index_video_bg.html` 測試
4. ✅ 如果滿意，替換 `index.html`
5. ✅ 上傳到你的網絡服務器

---

## 💡 提示

- 使用高質量但文件小的視頻以获得最佳結果
- 測試在不同網速下的性能
- 確保視頻內容與你的品牌相符
- 定期備份原始文件

---

**祝你的網站設計完美！** 🚀

如有任何問題，請檢查瀏覽器控制台 (F12) 中的錯誤信息。

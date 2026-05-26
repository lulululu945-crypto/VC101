# 🚀 Quick Start Guide - Video Background Website

## ⚡ 快速開始（3步完成）

### 步驟 1️⃣: 下載視頻
**最簡單的方法（Windows）：**
```bash
# 1. 雙擊 download_bg_video.bat
# 2. 粘貼你的 YouTube URL
# 3. 等待完成！
```

**或使用 Python（所有平台）：**
```bash
python download_bg_video.py
```

**或手動下載：**
- 訪問：https://www.4kdownload.com/ 或 https://y2mate.com/
- 下載 MP4 格式

### 步驟 2️⃣: 放置視頻
將視頻放在此位置：
```
VC101/
└── assets/
    └── video/
        └── bg-video.mp4
```

### 步驟 3️⃣: 使用網站
使用新文件替代舊文件：
```bash
# 重命名文件
ren index.html index_old.html
ren index_video_bg.html index.html

# 或直接在瀏覽器打開
http://localhost/VC101/index_video_bg.html
```

---

## 📦 文件說明

| 文件 | 用途 |
|------|------|
| `index_video_bg.html` | ✨ 新的視頻背景版本（主要文件） |
| `index.html` | 原始版本（保留備份） |
| `download_bg_video.bat` | 🪟 Windows 自動下載腳本 |
| `download_bg_video.py` | 🐍 Python 通用下載腳本 |
| `VIDEO_SETUP_GUIDE_ZH.md` | 📖 詳細中文設置指南 |
| `VIDEO_SETUP_GUIDE_EN.md` | 📖 詳細英文設置指南 |
| `assets/video/` | 📁 視頻文件夾 |

---

## ✨ 主要特性

✅ **全屏視頻背景** - 自動適應所有設備  
✅ **自動播放 & 循環** - 無需用戶交互  
✅ **優化排版** - 清晰的中英文混合字體  
✅ **高對比度** - 文字在視頻上清晰可見  
✅ **響應式設計** - 完美支持手機/平板/桌面  
✅ **性能優化** - 快速加載和流暢播放  
✅ **專業動畫** - 按鈕懸停效果和微交互  

---

## 🎨 自定義指南

### 修改文字顏色
編輯 `index_video_bg.html`，搜索並修改：
```html
<!-- 改變文字顏色 -->
<span class="text-white">文字</span>
<!-- 改為其他顏色，如 text-yellow-300, text-red-400 等 -->
```

### 調整視頻效果
找到 CSS 部分，修改：
```css
.video-bg-container video {
    opacity: 0.85;  /* 0-1，值越小越透明 */
    filter: brightness(0.75) contrast(1.1);  /* 調整亮度和對比度 */
}
```

### 改變強調色
在文件頂部的 Tailwind 配置中修改：
```javascript
colors: {
    brand: {
        blue: '#1E6FB9',  // 改變這些顏色
        green: '#4CAF7D',
        // ...
    }
}
```

---

## 📱 設備兼容性

| 設備 | 支持 | 備註 |
|------|------|------|
| 📱 iPhone | ✅ | 完美支持，自動靜音播放 |
| 📱 Android | ✅ | 完美支持 |
| 💻 Windows | ✅ | 完美支持 |
| 🖥️ Mac | ✅ | 完美支持 |
| 📺 大屏 | ✅ | 支持高分辨率 |

---

## 🎯 視頻推薦規格

| 項目 | 推薦值 | 範圍 |
|------|--------|------|
| 分辨率 | 1920×1080 | 1280×720 ~ 2560×1440 |
| 幀率 | 24fps | 24-60fps |
| 時長 | 15秒 | 5-60秒 |
| 文件大小 | 10MB | 5-30MB |
| 格式 | MP4 | MP4, WebM |
| 比例 | 16:9 | 16:9 推薦 |

---

## ❓ 常見問題

**Q: 視頻不播放？**  
A: 檢查文件路徑是否正確 (`assets/video/bg-video.mp4`)，重新下載或轉換視頻

**Q: 文字不清晰？**  
A: 增加覆蓋層的不透明度（改大 rgba 中的數值），或選擇亮度較高的視頻

**Q: 頁面加載緩慢？**  
A: 減小視頻文件大小，使用網頁優化工具，啟用 gzip 壓縮

**Q: 手機上不播放？**  
A: 大多數手機默認靜音播放，代碼已設置 `muted` 屬性，應該可以工作

---

## 🔍 故障排除

### 檢查瀏覽器控制台
按 `F12` 打開開發者工具 → Console 標籤
查看是否有紅色錯誤信息

### 常見錯誤
```
CORS error → 視頻文件路徑不正確
Failed to load → 文件不存在或格式不支持
Video not playing → 檢查瀏覽器設置或視頻格式
```

### 重置方法
1. 清空瀏覽器緩存（Ctrl+Shift+Delete）
2. 硬刷新頁面（Ctrl+Shift+R）
3. 在無痕模式下測試

---

## 📊 性能監控

查看頁面性能：
1. 打開 Chrome DevTools (F12)
2. 進入 Lighthouse 標籤
3. 點擊 "Generate report"

目標分數：
- Performance: > 80
- Accessibility: > 90
- Best Practices: > 90

---

## 📞 支持

如遇問題：
1. 檢查文件路徑和格式
2. 查閱詳細設置指南
3. 測試不同的視頻文件
4. 嘗試不同的瀏覽器

---

## 🎉 完成清單

- [ ] 已下載視頻
- [ ] 視頻放在 `assets/video/bg-video.mp4`
- [ ] 打開 `index_video_bg.html` 測試
- [ ] 文字清晰可見
- [ ] 所有按鈕正常工作
- [ ] 在手機上測試
- [ ] 準備上傳到服務器

---

**祝賀！你的視頻背景網站已準備就緒！🚀**

---

## 📚 更多資源

- [Tailwind CSS 文檔](https://tailwindcss.com)
- [FFmpeg 教程](https://ffmpeg.org/documentation.html)
- [Web 視頻最佳實踐](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/video)
- [性能優化指南](https://web.dev/performance/)

---

**版本**: 1.0  
**更新時間**: 2026年5月26日  
**語言**: 中文/English

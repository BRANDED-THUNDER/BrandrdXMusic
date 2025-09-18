import os
import re
import random

import aiofiles
import aiohttp

from BrandrdXMusic import app
from config import YOUTUBE_IMG_URL

<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Music Thumbnail</title>
  <style>
    body {
      background: #111;
      display: flex;
      justify-content: center;
      align-items: center;
      height: 100vh;
      margin: 0;
      font-family: Arial, sans-serif;
      color: #fff;
    }

    .thumbnail {
      width: 800px;
      background: rgba(0, 0, 0, 0.85);
      border-radius: 20px;
      padding: 20px;
      position: relative;
      overflow: hidden;
    }

    .thumbnail img {
      width: 300px;
      border-radius: 15px;
      float: right;
    }

    .playlist {
      float: left;
      width: 450px;
    }

    .playlist h1 {
      font-size: 40px;
      font-weight: bold;
      color: #ffcc00;
      margin: 10px 0;
      line-height: 1.2;
    }

    .playlist h2 {
      font-size: 22px;
      margin: 0;
      color: #fff;
    }

    .songs {
      margin-top: 15px;
      font-size: 14px;
      line-height: 1.6;
      color: #ddd;
      max-height: 350px;
      overflow-y: auto;
    }

    .songs::-webkit-scrollbar {
      width: 6px;
    }

    .songs::-webkit-scrollbar-thumb {
      background: #ffcc00;
      border-radius: 10px;
    }

    .footer {
      clear: both;
      margin-top: 20px;
      padding-top: 10px;
      border-top: 1px solid #444;
      display: flex;
      justify-content: space-between;
      align-items: center;
      font-size: 14px;
      color: #aaa;
    }

    .progress {
      width: 100%;
      height: 5px;
      background: #444;
      border-radius: 10px;
      margin: 8px 0;
      position: relative;
    }

    .progress-bar {
      width: 20%;
      height: 100%;
      background: #ffcc00;
      border-radius: 10px;
    }
  </style>
</head>
<body>

  <div class="thumbnail">
    <div class="playlist">
      <h1>LONG DRIVE</h1>
      <h2>BOLLYWOOD MIX <br> ARIJIT SINGH</h2>
      <div class="songs">
        <p>00:01 Apna Bana Le</p>
        <p>04:21 Pal Pal Dil Ke Paas</p>
        <p>08:13 Ve Mahi</p>
        <p>12:36 Kalank</p>
        <p>16:45 Phir Bhi Tumko Chaahunga</p>
        <p>21:25 Qaafirana</p>
        <p>25:36 Dekha Hazaro Dafaa</p>
        <p>30:15 Dil Na Jaane Ya</p>
        <p>34:50 Laal Ishq</p>
        <p>40:21 Shayad</p>
        <!-- add more as needed -->
      </div>
    </div>

    <img src="https://i.ibb.co/0c9R1N2/arijit.jpg" alt="Arijit Singh">

    <div class="footer">
      <span>Bollywood Chartbusters | 15M views</span>
      <span>1:55:45</span>
    </div>

    <div class="progress">
      <div class="progress-bar"></div>
    </div>
  </div>

</body>
</html>

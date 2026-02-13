import sys
import os
import re
import datetime
import shlex
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *

# --- DAFTAR PARTISI KRUSIAL UNTUK SMART BACKUP ---
SAFE_PARTS = ["nvram", "nvdata", "nvcfg", "protect1", "protect2", "seccfg"]

# --- PARTISI YANG MEMERLUKAN WAKTU LEBIH LAMA ---
SLOW_PARTITIONS = ["super", "tranfs", "userdata", "system", "vendor", "product"]

# --- MULTIPLE THEMES DENGAN ENHANCED STYLES ---
THEMES = {
    "Dark Purple": """
QWidget {
    background-color: #121212;
    color: #e0e0e0;
    font-family: 'Segoe UI';
    font-size: 13px;
}

QTabWidget::pane {
    border: 1px solid #333;
    background: #1e1e1e;
    border-radius: 8px;
    margin-top: 5px;
}

QTabBar::tab {
    background: #252525;
    padding: 12px 24px;
    margin-right: 4px;
    border-top-left-radius: 8px;
    border-top-right-radius: 8px;
    font-weight: 600;
    transition: all 0.3s ease;
}

QTabBar::tab:selected {
    background: qlineargradient(x1:0, y1:0, x2:0, y2:1, stop:0 #6200ee, stop:1 #4a00b3);
    color: white;
    border-bottom: 3px solid #bb86fc;
}

QTabBar::tab:hover {
    background: #2d2d2d;
}

QLineEdit {
    background-color: #2c2c2c;
    border: 1px solid #444;
    border-radius: 6px;
    padding: 10px;
    color: #fff;
    selection-background-color: #6200ee;
}

QLineEdit:focus {
    border: 2px solid #bb86fc;
    background-color: #333;
}

QPushButton {
    background-color: #333;
    border-radius: 6px;
    padding: 12px 20px;
    font-weight: bold;
    color: #fff;
    border: none;
    transition: all 0.2s ease;
}

QPushButton:hover {
    background-color: qlineargradient(x1:0, y1:0, x2:0, y2:1, stop:0 #444, stop:1 #3d3d3d);
    transform: translateY(-1px);
    box-shadow: 0 2px 8px rgba(98, 0, 238, 0.3);
}

QPushButton:pressed {
    transform: translateY(1px);
    box-shadow: 0 1px 3px rgba(0, 0, 0, 0.5);
}

QPushButton#actionBtn {
    background-color: qlineargradient(x1:0, y1:0, x2:0, y2:1, stop:0 #6200ee, stop:1 #4a00b3);
    color: white;
    border: none;
}

QPushButton#actionBtn:hover {
    background-color: qlineargradient(x1:0, y1:0, x2:0, y2:1, stop:0 #7c3ae5, stop:1 #5c2bc9);
    box-shadow: 0 4px 12px rgba(98, 0, 238, 0.5);
}

QPushButton#dangerBtn {
    background-color: qlineargradient(x1:0, y1:0, x2:0, y2:1, stop:0 #cf6679, stop:1 #b04a5a);
    color: white;
    border: none;
}

QPushButton#dangerBtn:hover {
    background-color: qlineargradient(x1:0, y1:0, x2:0, y2:1, stop:0 #e57373, stop:1 #c65c6c);
    box-shadow: 0 4px 12px rgba(207, 102, 121, 0.5);
}

QPushButton#cancelBtn {
    background-color: qlineargradient(x1:0, y1:0, x2:0, y2:1, stop:0 #555, stop:1 #444);
    color: #ff5252;
    border: 2px solid #ff5252;
}

QPushButton#cancelBtn:hover {
    background-color: qlineargradient(x1:0, y1:0, x2:0, y2:1, stop:0 #666, stop:1 #555);
    box-shadow: 0 4px 12px rgba(255, 82, 82, 0.3);
}

QListWidget {
    background-color: #1e1e1e;
    border: 1px solid #333;
    border-radius: 6px;
    outline: none;
    padding: 5px;
}

QListWidget::item {
    padding: 10px 12px;
    border-bottom: 1px solid #252525;
    border-radius: 4px;
    margin: 2px 0;
}

QListWidget::item:hover {
    background-color: #2a2a2a;
}

QListWidget::item:selected {
    background-color: qlineargradient(x1:0, y1:0, x2:0, y2:1, stop:0 #6200ee, stop:1 #4a00b3);
    color: white;
    border-left: 3px solid #bb86fc;
}

QTextEdit {
    background-color: #000;
    color: #00ff41;
    font-family: 'Consolas', 'Courier New';
    font-size: 11px;
    border: 1px solid #333;
    border-radius: 6px;
    padding: 10px;
    line-height: 1.4;
}

QLabel#header {
    font-size: 24px;
    font-weight: bold;
    color: #bb86fc;
    background: qlineargradient(x1:0, y1:0, x2:0, y2:1, stop:0 #6200ee, stop:1 #4a00b3);
    padding: 12px 20px;
    border-radius: 8px;
    margin-bottom: 10px;
}

QCheckBox {
    spacing: 12px;
    color: #e0e0e0;
    font-size: 13px;
}

QCheckBox::indicator {
    width: 24px;
    height: 24px;
    border: 3px solid #6200ee;
    border-radius: 6px;
    background-color: #2c2c2c;
}

QCheckBox::indicator:checked {
    background-color: qradialgradient(cx:0.5, cy:0.5, radius:0.5, fx:0.5, fy:0.5, stop:0 #6200ee, stop:1 #4a00b3);
    border: 3px solid #bb86fc;
}

QCheckBox::indicator:unchecked {
    background-color: #1e1e1e;
    border: 3px solid #666;
}

QCheckBox::indicator:hover {
    border: 3px solid #bb86fc;
    background-color: #333;
}

QScrollArea {
    background-color: #1e1e1e;
    border: none;
}

QScrollBar:vertical {
    background: #252525;
    width: 14px;
    border-radius: 7px;
    margin: 2px;
}

QScrollBar::handle:vertical {
    background: qlineargradient(x1:0, y1:0, x2:1, y2:0, stop:0 #555, stop:1 #666);
    border-radius: 7px;
    min-height: 30px;
    margin: 2px;
}

QScrollBar::handle:vertical:hover {
    background: qlineargradient(x1:0, y1:0, x2:1, y2:0, stop:0 #666, stop:1 #777);
}

QScrollBar::add-line:vertical, QScrollBar::sub-line:vertical {
    height: 0px;
}

QGroupBox {
    border: 1px solid #444;
    border-radius: 8px;
    margin-top: 15px;
    padding-top: 15px;
    font-weight: bold;
    background-color: #1a1a1a;
}

QGroupBox::title {
    subcontrol-origin: margin;
    left: 15px;
    padding: 0 10px;
    background-color: #252525;
    border-radius: 6px;
}

QSplitter::handle {
    background: qlineargradient(x1:0, y1:0, x2:1, y2:0, stop:0 #333, stop:1 #444, stop:2 #333);
    width: 6px;
    border-radius: 3px;
}

QComboBox {
    background-color: #2c2c2c;
    border: 1px solid #444;
    border-radius: 6px;
    padding: 8px 12px;
    color: #fff;
    min-width: 150px;
}

QComboBox:hover {
    border: 1px solid #bb86fc;
}

QComboBox::drop-down {
    border: none;
    width: 25px;
}

QComboBox QAbstractItemView {
    background-color: #252525;
    border: 1px solid #444;
    selection-background-color: #6200ee;
    selection-color: white;
}

QMessageBox {
    background-color: #1e1e1e;
}

QMessageBox QLabel {
    color: #e0e0e0;
}

QProgressBar {
    border: 1px solid #444;
    border-radius: 6px;
    text-align: center;
    background-color: #252525;
}

QProgressBar::chunk {
    background-color: qlineargradient(x1:0, y1:0, x2:0, y2:1, stop:0 #6200ee, stop:1 #4a00b3);
    border-radius: 5px;
}
""",
    "Dark Blue": """
QWidget {
    background-color: #0d1117;
    color: #c9d1d9;
    font-family: 'Segoe UI';
    font-size: 13px;
}

QTabWidget::pane {
    border: 1px solid #30363d;
    background: #161b22;
    border-radius: 8px;
    margin-top: 5px;
}

QTabBar::tab {
    background: #1c2128;
    padding: 12px 24px;
    margin-right: 4px;
    border-top-left-radius: 8px;
    border-top-right-radius: 8px;
    font-weight: 600;
}

QTabBar::tab:selected {
    background: qlineargradient(x1:0, y1:0, x2:0, y2:1, stop:0 #1f6feb, stop:1 #0d47a1);
    color: white;
    border-bottom: 3px solid #58a6ff;
}

QTabBar::tab:hover {
    background: #252b33;
}

QLineEdit {
    background-color: #0d1117;
    border: 1px solid #30363d;
    border-radius: 6px;
    padding: 10px;
    color: #c9d1d9;
    selection-background-color: #1f6feb;
}

QLineEdit:focus {
    border: 2px solid #58a6ff;
    background-color: #161b22;
}

QPushButton {
    background-color: #21262d;
    border-radius: 6px;
    padding: 12px 20px;
    font-weight: bold;
    color: #c9d1d9;
    border: none;
}

QPushButton:hover {
    background-color: qlineargradient(x1:0, y1:0, x2:0, y2:1, stop:0 #30363d, stop:1 #2a2f36);
    transform: translateY(-1px);
    box-shadow: 0 2px 8px rgba(31, 111, 235, 0.3);
}

QPushButton:pressed {
    transform: translateY(1px);
    box-shadow: 0 1px 3px rgba(0, 0, 0, 0.5);
}

QPushButton#actionBtn {
    background-color: qlineargradient(x1:0, y1:0, x2:0, y2:1, stop:0 #238636, stop:1 #1a6529);
    color: white;
}

QPushButton#actionBtn:hover {
    background-color: qlineargradient(x1:0, y1:0, x2:0, y2:1, stop:0 #2ea043, stop:1 #238636);
    box-shadow: 0 4px 12px rgba(35, 134, 54, 0.5);
}

QPushButton#dangerBtn {
    background-color: qlineargradient(x1:0, y1:0, x2:0, y2:1, stop:0 #da3633, stop:1 #b02a29);
    color: white;
}

QPushButton#dangerBtn:hover {
    background-color: qlineargradient(x1:0, y1:0, x2:0, y2:1, stop:0 #f85149, stop:1 #da3633);
    box-shadow: 0 4px 12px rgba(218, 54, 51, 0.5);
}

QPushButton#cancelBtn {
    background-color: qlineargradient(x1:0, y1:0, x2:0, y2:1, stop:0 #6e7681, stop:1 #575e66);
    color: #ff7b72;
    border: 2px solid #ff7b72;
}

QPushButton#cancelBtn:hover {
    background-color: qlineargradient(x1:0, y1:0, x2:0, y2:1, stop:0 #8b949e, stop:1 #6e7681);
    box-shadow: 0 4px 12px rgba(255, 123, 114, 0.3);
}

QListWidget {
    background-color: #161b22;
    border: 1px solid #30363d;
    border-radius: 6px;
    outline: none;
    padding: 5px;
}

QListWidget::item {
    padding: 10px 12px;
    border-bottom: 1px solid #21262d;
    border-radius: 4px;
    margin: 2px 0;
}

QListWidget::item:hover {
    background-color: #252b33;
}

QListWidget::item:selected {
    background-color: qlineargradient(x1:0, y1:0, x2:0, y2:1, stop:0 #1f6feb, stop:1 #0d47a1);
    color: white;
    border-left: 3px solid #58a6ff;
}

QTextEdit {
    background-color: #010409;
    color: #58a6ff;
    font-family: 'Consolas', 'Courier New';
    font-size: 11px;
    border: 1px solid #30363d;
    border-radius: 6px;
    padding: 10px;
    line-height: 1.4;
}

QLabel#header {
    font-size: 24px;
    font-weight: bold;
    color: #58a6ff;
    background: qlineargradient(x1:0, y1:0, x2:0, y2:1, stop:0 #1f6feb, stop:1 #0d47a1);
    padding: 12px 20px;
    border-radius: 8px;
    margin-bottom: 10px;
}

QCheckBox {
    spacing: 12px;
    color: #c9d1d9;
}

QCheckBox::indicator {
    width: 24px;
    height: 24px;
    border: 3px solid #1f6feb;
    border-radius: 6px;
    background-color: #0d1117;
}

QCheckBox::indicator:checked {
    background-color: qradialgradient(cx:0.5, cy:0.5, radius:0.5, fx:0.5, fy:0.5, stop:0 #238636, stop:1 #1a6529);
    border: 3px solid #238636;
}

QCheckBox::indicator:unchecked {
    background-color: #161b22;
    border: 3px solid #6e7681;
}

QCheckBox::indicator:hover {
    border: 3px solid #58a6ff;
    background-color: #21262d;
}

QScrollArea {
    background-color: #161b22;
    border: none;
}

QScrollBar:vertical {
    background: #21262d;
    width: 14px;
    border-radius: 7px;
    margin: 2px;
}

QScrollBar::handle:vertical {
    background: qlineargradient(x1:0, y1:0, x2:1, y2:0, stop:0 #6e7681, stop:1 #8b949e);
    border-radius: 7px;
    min-height: 30px;
    margin: 2px;
}

QScrollBar::handle:vertical:hover {
    background: qlineargradient(x1:0, y1:0, x2:1, y2:0, stop:0 #8b949e, stop:1 #c9d1d9);
}

QScrollBar::add-line:vertical, QScrollBar::sub-line:vertical {
    height: 0px;
}

QGroupBox {
    border: 1px solid #30363d;
    border-radius: 8px;
    margin-top: 15px;
    padding-top: 15px;
    font-weight: bold;
    background-color: #11151c;
}

QGroupBox::title {
    subcontrol-origin: margin;
    left: 15px;
    padding: 0 10px;
    background-color: #1c2128;
    border-radius: 6px;
}

QSplitter::handle {
    background: qlineargradient(x1:0, y1:0, x2:1, y2:0, stop:0 #30363d, stop:1 #444b56, stop:2 #30363d);
    width: 6px;
    border-radius: 3px;
}

QComboBox {
    background-color: #0d1117;
    border: 1px solid #30363d;
    border-radius: 6px;
    padding: 8px 12px;
    color: #c9d1d9;
    min-width: 150px;
}

QComboBox:hover {
    border: 1px solid #58a6ff;
}

QComboBox::drop-down {
    border: none;
    width: 25px;
}

QComboBox QAbstractItemView {
    background-color: #1c2128;
    border: 1px solid #30363d;
    selection-background-color: #1f6feb;
    selection-color: white;
}

QMessageBox {
    background-color: #161b22;
}

QMessageBox QLabel {
    color: #c9d1d9;
}

QProgressBar {
    border: 1px solid #30363d;
    border-radius: 6px;
    text-align: center;
    background-color: #1c2128;
}

QProgressBar::chunk {
    background-color: qlineargradient(x1:0, y1:0, x2:0, y2:1, stop:0 #238636, stop:1 #1a6529);
    border-radius: 5px;
}
""",
    "Cyberpunk": """
QWidget {
    background-color: #0a0e27;
    color: #00ffff;
    font-family: 'Segoe UI';
    font-size: 13px;
}

QTabWidget::pane {
    border: 1px solid #ff00ff;
    background: #16213e;
    border-radius: 8px;
    margin-top: 5px;
}

QTabBar::tab {
    background: #1a1a2e;
    padding: 12px 24px;
    margin-right: 4px;
    border-top-left-radius: 8px;
    border-top-right-radius: 8px;
    font-weight: 600;
}

QTabBar::tab:selected {
    background: qlineargradient(x1:0, y1:0, x2:0, y2:1, stop:0 #ff00ff, stop:1 #cc00cc);
    color: white;
    border-bottom: 3px solid #00ffff;
}

QTabBar::tab:hover {
    background: #25253e;
}

QLineEdit {
    background-color: #16213e;
    border: 2px solid #00ffff;
    border-radius: 6px;
    padding: 10px;
    color: #00ffff;
    selection-background-color: #ff00ff;
}

QLineEdit:focus {
    border: 2px solid #ff00ff;
    background-color: #1a1a2e;
    box-shadow: 0 0 10px rgba(0, 255, 255, 0.3);
}

QPushButton {
    background-color: #1a1a2e;
    border-radius: 6px;
    padding: 12px 20px;
    font-weight: bold;
    color: #00ffff;
    border: 2px solid #00ffff;
}

QPushButton:hover {
    background-color: qlineargradient(x1:0, y1:0, x2:0, y2:1, stop:0 #0f3460, stop:1 #1a1a2e);
    transform: translateY(-1px);
    box-shadow: 0 0 15px rgba(0, 255, 255, 0.5);
}

QPushButton:pressed {
    transform: translateY(1px);
    box-shadow: 0 0 5px rgba(0, 255, 255, 0.8);
}

QPushButton#actionBtn {
    background-color: qlineargradient(x1:0, y1:0, x2:0, y2:1, stop:0 #ff00ff, stop:1 #cc00cc);
    color: white;
    border: none;
}

QPushButton#actionBtn:hover {
    background-color: qlineargradient(x1:0, y1:0, x2:0, y2:1, stop:0 #ff33ff, stop:1 #ff00ff);
    box-shadow: 0 0 20px rgba(255, 0, 255, 0.7);
}

QPushButton#dangerBtn {
    background-color: qlineargradient(x1:0, y1:0, x2:0, y2:1, stop:0 #ff006e, stop:1 #cc0059);
    color: white;
    border: none;
}

QPushButton#dangerBtn:hover {
    background-color: qlineargradient(x1:0, y1:0, x2:0, y2:1, stop:0 #ff3385, stop:1 #ff006e);
    box-shadow: 0 0 20px rgba(255, 0, 110, 0.7);
}

QPushButton#cancelBtn {
    background-color: qlineargradient(x1:0, y1:0, x2:0, y2:1, stop:0 #e94560, stop:1 #b8364c);
    color: white;
    border: 2px solid #ff6b81;
}

QPushButton#cancelBtn:hover {
    background-color: qlineargradient(x1:0, y1:0, x2:0, y2:1, stop:0 #ff5269, stop:1 #e94560);
    box-shadow: 0 0 20px rgba(233, 69, 96, 0.5);
}

QListWidget {
    background-color: #16213e;
    border: 2px solid #00ffff;
    border-radius: 6px;
    outline: none;
    padding: 5px;
}

QListWidget::item {
    padding: 10px 12px;
    border-bottom: 1px solid #1a1a2e;
    border-radius: 4px;
    margin: 2px 0;
}

QListWidget::item:hover {
    background-color: #25253e;
    border-left: 3px solid #00ffff;
}

QListWidget::item:selected {
    background-color: qlineargradient(x1:0, y1:0, x2:0, y2:1, stop:0 #ff00ff, stop:1 #cc00cc);
    color: white;
    border-left: 4px solid #00ffff;
}

QTextEdit {
    background-color: #000;
    color: #ff00ff;
    font-family: 'Consolas', 'Courier New';
    font-size: 11px;
    border: 2px solid #00ffff;
    border-radius: 6px;
    padding: 10px;
    line-height: 1.4;
}

QLabel#header {
    font-size: 24px;
    font-weight: bold;
    color: #ff00ff;
    background: qlineargradient(x1:0, y1:0, x2:0, y2:1, stop:0 #ff00ff, stop:1 #cc00cc);
    padding: 12px 20px;
    border-radius: 8px;
    margin-bottom: 10px;
    border: 2px solid #00ffff;
    box-shadow: 0 0 20px rgba(255, 0, 255, 0.5);
}

QCheckBox {
    spacing: 12px;
    color: #00ffff;
}

QCheckBox::indicator {
    width: 24px;
    height: 24px;
    border: 3px solid #ff00ff;
    border-radius: 6px;
    background-color: #16213e;
}

QCheckBox::indicator:checked {
    background-color: qradialgradient(cx:0.5, cy:0.5, radius:0.5, fx:0.5, fy:0.5, stop:0 #ff00ff, stop:1 #cc00cc);
    border: 3px solid #ff00ff;
}

QCheckBox::indicator:unchecked {
    background-color: #1a1a2e;
    border: 3px solid #00ffff;
}

QCheckBox::indicator:hover {
    border: 3px solid #00ffff;
    background-color: #0f3460;
}

QScrollArea {
    background-color: #16213e;
    border: none;
}

QScrollBar:vertical {
    background: #1a1a2e;
    width: 14px;
    border-radius: 7px;
    margin: 2px;
    border: 1px solid #00ffff;
}

QScrollBar::handle:vertical {
    background: qlineargradient(x1:0, y1:0, x2:1, y2:0, stop:0 #ff00ff, stop:1 #cc00cc);
    border-radius: 7px;
    min-height: 30px;
    margin: 2px;
}

QScrollBar::handle:vertical:hover {
    background: qlineargradient(x1:0, y1:0, x2:1, y2:0, stop:0 #ff33ff, stop:1 #ff00ff);
    border: 2px solid #00ffff;
}

QScrollBar::add-line:vertical, QScrollBar::sub-line:vertical {
    height: 0px;
}

QGroupBox {
    border: 2px solid #00ffff;
    border-radius: 8px;
    margin-top: 15px;
    padding-top: 15px;
    font-weight: bold;
    color: #00ffff;
    background-color: rgba(22, 33, 62, 0.5);
}

QGroupBox::title {
    subcontrol-origin: margin;
    left: 15px;
    padding: 0 10px;
    background-color: #1a1a2e;
    border-radius: 6px;
    color: #00ffff;
}

QSplitter::handle {
    background: qlineargradient(x1:0, y1:0, x2:1, y2:0, stop:0 #ff00ff, stop:1 #00ffff, stop:2 #ff00ff);
    width: 6px;
    border-radius: 3px;
}

QComboBox {
    background-color: #16213e;
    border: 2px solid #00ffff;
    border-radius: 6px;
    padding: 8px 12px;
    color: #00ffff;
    min-width: 150px;
}

QComboBox:hover {
    border: 2px solid #ff00ff;
    box-shadow: 0 0 10px rgba(0, 255, 255, 0.5);
}

QComboBox::drop-down {
    border: none;
    width: 25px;
}

QComboBox QAbstractItemView {
    background-color: #1a1a2e;
    border: 2px solid #00ffff;
    selection-background-color: #ff00ff;
    selection-color: white;
}

QMessageBox {
    background-color: #16213e;
    border: 2px solid #00ffff;
}

QMessageBox QLabel {
    color: #00ffff;
}

QProgressBar {
    border: 2px solid #00ffff;
    border-radius: 6px;
    text-align: center;
    background-color: #1a1a2e;
}

QProgressBar::chunk {
    background-color: qlineargradient(x1:0, y1:0, x2:0, y2:1, stop:0 #ff00ff, stop:1 #cc00cc);
    border-radius: 5px;
}
""",
    "Matrix Green": """
QWidget {
    background-color: #000000;
    color: #00ff00;
    font-family: 'Segoe UI';
    font-size: 13px;
}

QTabWidget::pane {
    border: 1px solid #003b00;
    background: #001a00;
    border-radius: 8px;
    margin-top: 5px;
}

QTabBar::tab {
    background: #001400;
    padding: 12px 24px;
    margin-right: 4px;
    border-top-left-radius: 8px;
    border-top-right-radius: 8px;
    font-weight: 600;
    color: #00ff00;
}

QTabBar::tab:selected {
    background: qlineargradient(x1:0, y1:0, x2:0, y2:1, stop:0 #00ff00, stop:1 #00aa00);
    color: black;
    border-bottom: 3px solid #00ff00;
}

QTabBar::tab:hover {
    background: #003b00;
}

QLineEdit {
    background-color: #001a00;
    border: 1px solid #00ff00;
    border-radius: 6px;
    padding: 10px;
    color: #00ff00;
    selection-background-color: #00ff00;
}

QLineEdit:focus {
    border: 2px solid #00ff00;
    background-color: #002a00;
}

QPushButton {
    background-color: #001400;
    border-radius: 6px;
    padding: 12px 20px;
    font-weight: bold;
    color: #00ff00;
    border: 1px solid #00ff00;
}

QPushButton:hover {
    background-color: qlineargradient(x1:0, y1:0, x2:0, y2:1, stop:0 #003b00, stop:1 #002a00);
    transform: translateY(-1px);
    box-shadow: 0 0 15px rgba(0, 255, 0, 0.5);
}

QPushButton:pressed {
    transform: translateY(1px);
    box-shadow: 0 0 5px rgba(0, 255, 0, 0.8);
}

QPushButton#actionBtn {
    background-color: qlineargradient(x1:0, y1:0, x2:0, y2:1, stop:0 #00ff00, stop:1 #00aa00);
    color: black;
    border: none;
}

QPushButton#actionBtn:hover {
    background-color: qlineargradient(x1:0, y1:0, x2:0, y2:1, stop:0 #33ff33, stop:1 #00ff00);
    box-shadow: 0 0 20px rgba(0, 255, 0, 0.7);
}

QPushButton#dangerBtn {
    background-color: qlineargradient(x1:0, y1:0, x2:0, y2:1, stop:0 #ff0000, stop:1 #cc0000);
    color: white;
    border: none;
}

QPushButton#dangerBtn:hover {
    background-color: qlineargradient(x1:0, y1:0, x2:0, y2:1, stop:0 #ff3333, stop:1 #ff0000);
    box-shadow: 0 0 20px rgba(255, 0, 0, 0.7);
}

QPushButton#cancelBtn {
    background-color: qlineargradient(x1:0, y1:0, x2:0, y2:1, stop:0 #660000, stop:1 #330000);
    color: #ff0000;
    border: 2px solid #ff0000;
}

QPushButton#cancelBtn:hover {
    background-color: qlineargradient(x1:0, y1:0, x2:0, y2:1, stop:0 #990000, stop:1 #660000);
    box-shadow: 0 0 20px rgba(255, 0, 0, 0.5);
}

QListWidget {
    background-color: #001a00;
    border: 1px solid #00ff00;
    border-radius: 6px;
    outline: none;
    padding: 5px;
}

QListWidget::item {
    padding: 10px 12px;
    border-bottom: 1px solid #001400;
    border-radius: 4px;
    margin: 2px 0;
}

QListWidget::item:hover {
    background-color: #003b00;
    border-left: 3px solid #00ff00;
}

QListWidget::item:selected {
    background-color: qlineargradient(x1:0, y1:0, x2:0, y2:1, stop:0 #00ff00, stop:1 #00aa00);
    color: black;
    border-left: 4px solid #00ff00;
}

QTextEdit {
    background-color: #000;
    color: #00ff00;
    font-family: 'Consolas', 'Courier New';
    font-size: 11px;
    border: 1px solid #00ff00;
    border-radius: 6px;
    padding: 10px;
    line-height: 1.4;
}

QLabel#header {
    font-size: 24px;
    font-weight: bold;
    color: #00ff00;
    background: qlineargradient(x1:0, y1:0, x2:0, y2:1, stop:0 #00ff00, stop:1 #00aa00);
    padding: 12px 20px;
    border-radius: 8px;
    margin-bottom: 10px;
    border: 1px solid #00ff00;
}

QCheckBox {
    spacing: 12px;
    color: #00ff00;
}

QCheckBox::indicator {
    width: 24px;
    height: 24px;
    border: 3px solid #00ff00;
    border-radius: 6px;
    background-color: #001a00;
}

QCheckBox::indicator:checked {
    background-color: qradialgradient(cx:0.5, cy:0.5, radius:0.5, fx:0.5, fy:0.5, stop:0 #00ff00, stop:1 #00aa00);
    border: 3px solid #00ff00;
}

QCheckBox::indicator:unchecked {
    background-color: #001400;
    border: 3px solid #00aa00;
}

QCheckBox::indicator:hover {
    border: 3px solid #00ff00;
    background-color: #003b00;
}

QScrollArea {
    background-color: #001a00;
    border: none;
}

QScrollBar:vertical {
    background: #001400;
    width: 14px;
    border-radius: 7px;
    margin: 2px;
    border: 1px solid #00ff00;
}

QScrollBar::handle:vertical {
    background: qlineargradient(x1:0, y1:0, x2:1, y2:0, stop:0 #00ff00, stop:1 #00aa00);
    border-radius: 7px;
    min-height: 30px;
    margin: 2px;
}

QScrollBar::handle:vertical:hover {
    background: qlineargradient(x1:0, y1:0, x2:1, y2:0, stop:0 #33ff33, stop:1 #00ff00);
    border: 2px solid #00ff00;
}

QScrollBar::add-line:vertical, QScrollBar::sub-line:vertical {
    height: 0px;
}

QGroupBox {
    border: 1px solid #00ff00;
    border-radius: 8px;
    margin-top: 15px;
    padding-top: 15px;
    font-weight: bold;
    color: #00ff00;
    background-color: rgba(0, 26, 0, 0.7);
}

QGroupBox::title {
    subcontrol-origin: margin;
    left: 15px;
    padding: 0 10px;
    background-color: #001400;
    border-radius: 6px;
    color: #00ff00;
}

QSplitter::handle {
    background: qlineargradient(x1:0, y1:0, x2:1, y2:0, stop:0 #00ff00, stop:1 #00aa00, stop:2 #00ff00);
    width: 6px;
    border-radius: 3px;
}

QComboBox {
    background-color: #001a00;
    border: 1px solid #00ff00;
    border-radius: 6px;
    padding: 8px 12px;
    color: #00ff00;
    min-width: 150px;
}

QComboBox:hover {
    border: 2px solid #33ff33;
    box-shadow: 0 0 10px rgba(0, 255, 0, 0.5);
}

QComboBox::drop-down {
    border: none;
    width: 25px;
}

QComboBox QAbstractItemView {
    background-color: #001400;
    border: 1px solid #00ff00;
    selection-background-color: #00ff00;
    selection-color: black;
}

QMessageBox {
    background-color: #001a00;
    border: 1px solid #00ff00;
}

QMessageBox QLabel {
    color: #00ff00;
}

QProgressBar {
    border: 1px solid #00ff00;
    border-radius: 6px;
    text-align: center;
    background-color: #001400;
}

QProgressBar::chunk {
    background-color: qlineargradient(x1:0, y1:0, x2:0, y2:1, stop:0 #00ff00, stop:1 #00aa00);
    border-radius: 5px;
}
""",
    "Sunset Orange": """
QWidget {
    background-color: #1a1a1a;
    color: #ffd7b5;
    font-family: 'Segoe UI';
    font-size: 13px;
}

QTabWidget::pane {
    border: 1px solid #ff6b35;
    background: #2d2d2d;
    border-radius: 8px;
    margin-top: 5px;
}

QTabBar::tab {
    background: #242424;
    padding: 12px 24px;
    margin-right: 4px;
    border-top-left-radius: 8px;
    border-top-right-radius: 8px;
    font-weight: 600;
    color: #ff9a76;
}

QTabBar::tab:selected {
    background: qlineargradient(x1:0, y1:0, x2:0, y2:1, stop:0 #ff6b35, stop:1 #e63946);
    color: white;
    border-bottom: 3px solid #ffd7b5;
}

QTabBar::tab:hover {
    background: #3d3d3d;
}

QLineEdit {
    background-color: #2d2d2d;
    border: 1px solid #ff6b35;
    border-radius: 6px;
    padding: 10px;
    color: #ffd7b5;
    selection-background-color: #ff6b35;
}

QLineEdit:focus {
    border: 2px solid #ffd7b5;
    background-color: #3d3d3d;
}

QPushButton {
    background-color: #3d3d3d;
    border-radius: 6px;
    padding: 12px 20px;
    font-weight: bold;
    color: #ffd7b5;
    border: 1px solid #ff6b35;
}

QPushButton:hover {
    background-color: qlineargradient(x1:0, y1:0, x2:0, y2:1, stop:0 #4d4d4d, stop:1 #3d3d3d);
    transform: translateY(-1px);
    box-shadow: 0 2px 8px rgba(255, 107, 53, 0.5);
}

QPushButton:pressed {
    transform: translateY(1px);
    box-shadow: 0 1px 3px rgba(0, 0, 0, 0.5);
}

QPushButton#actionBtn {
    background-color: qlineargradient(x1:0, y1:0, x2:0, y2:1, stop:0 #ff6b35, stop:1 #e63946);
    color: white;
    border: none;
}

QPushButton#actionBtn:hover {
    background-color: qlineargradient(x1:0, y1:0, x2:0, y2:1, stop:0 #ff9a76, stop:1 #ff6b35);
    box-shadow: 0 4px 12px rgba(255, 107, 53, 0.7);
}

QPushButton#dangerBtn {
    background-color: qlineargradient(x1:0, y1:0, x2:0, y2:1, stop:0 #e63946, stop:1 #c1121f);
    color: white;
    border: none;
}

QPushButton#dangerBtn:hover {
    background-color: qlineargradient(x1:0, y1:0, x2:0, y2:1, stop:0 #ff5252, stop:1 #e63946);
    box-shadow: 0 4px 12px rgba(230, 57, 70, 0.7);
}

QPushButton#cancelBtn {
    background-color: qlineargradient(x1:0, y1:0, x2:0, y2:1, stop:0 #f77f00, stop:1 #d62828);
    color: white;
    border: 2px solid #ff9a76;
}

QPushButton#cancelBtn:hover {
    background-color: qlineargradient(x1:0, y1:0, x2:0, y2:1, stop:0 #ff9a76, stop:1 #f77f00);
    box-shadow: 0 4px 12px rgba(247, 127, 0, 0.5);
}

QListWidget {
    background-color: #2d2d2d;
    border: 1px solid #ff6b35;
    border-radius: 6px;
    outline: none;
    padding: 5px;
}

QListWidget::item {
    padding: 10px 12px;
    border-bottom: 1px solid #3d3d3d;
    border-radius: 4px;
    margin: 2px 0;
}

QListWidget::item:hover {
    background-color: #4d4d4d;
}

QListWidget::item:selected {
    background-color: qlineargradient(x1:0, y1:0, x2:0, y2:1, stop:0 #ff6b35, stop:1 #e63946);
    color: white;
    border-left: 3px solid #ffd7b5;
}

QTextEdit {
    background-color: #1a1a1a;
    color: #ff9a76;
    font-family: 'Consolas', 'Courier New';
    font-size: 11px;
    border: 1px solid #ff6b35;
    border-radius: 6px;
    padding: 10px;
    line-height: 1.4;
}

QLabel#header {
    font-size: 24px;
    font-weight: bold;
    color: #ff6b35;
    background: qlineargradient(x1:0, y1:0, x2:0, y2:1, stop:0 #ff6b35, stop:1 #e63946);
    padding: 12px 20px;
    border-radius: 8px;
    margin-bottom: 10px;
}

QCheckBox {
    spacing: 12px;
    color: #ffd7b5;
}

QCheckBox::indicator {
    width: 24px;
    height: 24px;
    border: 3px solid #ff6b35;
    border-radius: 6px;
    background-color: #2d2d2d;
}

QCheckBox::indicator:checked {
    background-color: qradialgradient(cx:0.5, cy:0.5, radius:0.5, fx:0.5, fy:0.5, stop:0 #ff6b35, stop:1 #e63946);
    border: 3px solid #ff6b35;
}

QCheckBox::indicator:unchecked {
    background-color: #3d3d3d;
    border: 3px solid #ff9a76;
}

QCheckBox::indicator:hover {
    border: 3px solid #ffd7b5;
    background-color: #4d4d4d;
}

QScrollArea {
    background-color: #2d2d2d;
    border: none;
}

QScrollBar:vertical {
    background: #3d3d3d;
    width: 14px;
    border-radius: 7px;
    margin: 2px;
}

QScrollBar::handle:vertical {
    background: qlineargradient(x1:0, y1:0, x2:1, y2:0, stop:0 #ff6b35, stop:1 #e63946);
    border-radius: 7px;
    min-height: 30px;
    margin: 2px;
}

QScrollBar::handle:vertical:hover {
    background: qlineargradient(x1:0, y1:0, x2:1, y2:0, stop:0 #ff9a76, stop:1 #ff6b35);
}

QScrollBar::add-line:vertical, QScrollBar::sub-line:vertical {
    height: 0px;
}

QGroupBox {
    border: 1px solid #ff6b35;
    border-radius: 8px;
    margin-top: 15px;
    padding-top: 15px;
    font-weight: bold;
    background-color: rgba(45, 45, 45, 0.8);
}

QGroupBox::title {
    subcontrol-origin: margin;
    left: 15px;
    padding: 0 10px;
    background-color: #242424;
    border-radius: 6px;
    color: #ff9a76;
}

QSplitter::handle {
    background: qlineargradient(x1:0, y1:0, x2:1, y2:0, stop:0 #ff6b35, stop:1 #ffd7b5, stop:2 #ff6b35);
    width: 6px;
    border-radius: 3px;
}

QComboBox {
    background-color: #2d2d2d;
    border: 1px solid #ff6b35;
    border-radius: 6px;
    padding: 8px 12px;
    color: #ffd7b5;
    min-width: 150px;
}

QComboBox:hover {
    border: 1px solid #ffd7b5;
}

QComboBox::drop-down {
    border: none;
    width: 25px;
}

QComboBox QAbstractItemView {
    background-color: #242424;
    border: 1px solid #ff6b35;
    selection-background-color: #ff6b35;
    selection-color: white;
}

QMessageBox {
    background-color: #2d2d2d;
}

QMessageBox QLabel {
    color: #ffd7b5;
}

QProgressBar {
    border: 1px solid #ff6b35;
    border-radius: 6px;
    text-align: center;
    background-color: #242424;
}

QProgressBar::chunk {
    background-color: qlineargradient(x1:0, y1:0, x2:0, y2:1, stop:0 #ff6b35, stop:1 #e63946);
    border-radius: 5px;
}
""",
    "Ocean Blue": """
QWidget {
    background-color: #001f3f;
    color: #7fdbff;
    font-family: 'Segoe UI';
    font-size: 13px;
}

QTabWidget::pane {
    border: 1px solid #0074d9;
    background: #002f5f;
    border-radius: 8px;
    margin-top: 5px;
}

QTabBar::tab {
    background: #003a6f;
    padding: 12px 24px;
    margin-right: 4px;
    border-top-left-radius: 8px;
    border-top-right-radius: 8px;
    font-weight: 600;
    color: #7fdbff;
}

QTabBar::tab:selected {
    background: qlineargradient(x1:0, y1:0, x2:0, y2:1, stop:0 #0074d9, stop:1 #0047a0);
    color: white;
    border-bottom: 3px solid #7fdbff;
}

QTabBar::tab:hover {
    background: #004f8f;
}

QLineEdit {
    background-color: #002f5f;
    border: 1px solid #0074d9;
    border-radius: 6px;
    padding: 10px;
    color: #7fdbff;
    selection-background-color: #0074d9;
}

QLineEdit:focus {
    border: 2px solid #7fdbff;
    background-color: #003f7f;
}

QPushButton {
    background-color: #003f7f;
    border-radius: 6px;
    padding: 12px 20px;
    font-weight: bold;
    color: #7fdbff;
    border: 1px solid #0074d9;
}

QPushButton:hover {
    background-color: qlineargradient(x1:0, y1:0, x2:0, y2:1, stop:0 #004f8f, stop:1 #003f7f);
    transform: translateY(-1px);
    box-shadow: 0 2px 8px rgba(0, 116, 217, 0.5);
}

QPushButton:pressed {
    transform: translateY(1px);
    box-shadow: 0 1px 3px rgba(0, 0, 0, 0.5);
}

QPushButton#actionBtn {
    background-color: qlineargradient(x1:0, y1:0, x2:0, y2:1, stop:0 #0074d9, stop:1 #0047a0);
    color: white;
    border: none;
}

QPushButton#actionBtn:hover {
    background-color: qlineargradient(x1:0, y1:0, x2:0, y2:1, stop:0 #39cccc, stop:1 #0074d9);
    box-shadow: 0 4px 12px rgba(0, 116, 217, 0.7);
}

QPushButton#dangerBtn {
    background-color: qlineargradient(x1:0, y1:0, x2:0, y2:1, stop:0 #ff4136, stop:1 #cc0000);
    color: white;
    border: none;
}

QPushButton#dangerBtn:hover {
    background-color: qlineargradient(x1:0, y1:0, x2:0, y2:1, stop:0 #ff6347, stop:1 #ff4136);
    box-shadow: 0 4px 12px rgba(255, 65, 54, 0.7);
}

QPushButton#cancelBtn {
    background-color: qlineargradient(x1:0, y1:0, x2:0, y2:1, stop:0 #ff851b, stop:1 #e65100);
    color: white;
    border: 2px solid #ff851b;
}

QPushButton#cancelBtn:hover {
    background-color: qlineargradient(x1:0, y1:0, x2:0, y2:1, stop:0 #ffa726, stop:1 #ff851b);
    box-shadow: 0 4px 12px rgba(255, 133, 27, 0.5);
}

QListWidget {
    background-color: #002f5f;
    border: 1px solid #0074d9;
    border-radius: 6px;
    outline: none;
    padding: 5px;
}

QListWidget::item {
    padding: 10px 12px;
    border-bottom: 1px solid #003f7f;
    border-radius: 4px;
    margin: 2px 0;
}

QListWidget::item:hover {
    background-color: #004f8f;
}

QListWidget::item:selected {
    background-color: qlineargradient(x1:0, y1:0, x2:0, y2:1, stop:0 #0074d9, stop:1 #0047a0);
    color: white;
    border-left: 3px solid #7fdbff;
}

QTextEdit {
    background-color: #001020;
    color: #39cccc;
    font-family: 'Consolas', 'Courier New';
    font-size: 11px;
    border: 1px solid #0074d9;
    border-radius: 6px;
    padding: 10px;
    line-height: 1.4;
}

QLabel#header {
    font-size: 24px;
    font-weight: bold;
    color: #7fdbff;
    background: qlineargradient(x1:0, y1:0, x2:0, y2:1, stop:0 #0074d9, stop:1 #0047a0);
    padding: 12px 20px;
    border-radius: 8px;
    margin-bottom: 10px;
}

QCheckBox {
    spacing: 12px;
    color: #7fdbff;
}

QCheckBox::indicator {
    width: 24px;
    height: 24px;
    border: 3px solid #0074d9;
    border-radius: 6px;
    background-color: #002f5f;
}

QCheckBox::indicator:checked {
    background-color: qradialgradient(cx:0.5, cy:0.5, radius:0.5, fx:0.5, fy:0.5, stop:0 #0074d9, stop:1 #0047a0);
    border: 3px solid #0074d9;
}

QCheckBox::indicator:unchecked {
    background-color: #003f7f;
    border: 3px solid #39cccc;
}

QCheckBox::indicator:hover {
    border: 3px solid #7fdbff;
    background-color: #004f8f;
}

QScrollArea {
    background-color: #002f5f;
    border: none;
}

QScrollBar:vertical {
    background: #003f7f;
    width: 14px;
    border-radius: 7px;
    margin: 2px;
}

QScrollBar::handle:vertical {
    background: qlineargradient(x1:0, y1:0, x2:1, y2:0, stop:0 #0074d9, stop:1 #39cccc);
    border-radius: 7px;
    min-height: 30px;
    margin: 2px;
}

QScrollBar::handle:vertical:hover {
    background: qlineargradient(x1:0, y1:0, x2:1, y2:0, stop:0 #39cccc, stop:1 #7fdbff);
}

QScrollBar::add-line:vertical, QScrollBar::sub-line:vertical {
    height: 0px;
}

QGroupBox {
    border: 1px solid #0074d9;
    border-radius: 8px;
    margin-top: 15px;
    padding-top: 15px;
    font-weight: bold;
    background-color: rgba(0, 47, 95, 0.8);
}

QGroupBox::title {
    subcontrol-origin: margin;
    left: 15px;
    padding: 0 10px;
    background-color: #003a6f;
    border-radius: 6px;
    color: #7fdbff;
}

QSplitter::handle {
    background: qlineargradient(x1:0, y1:0, x2:1, y2:0, stop:0 #0074d9, stop:1 #7fdbff, stop:2 #0074d9);
    width: 6px;
    border-radius: 3px;
}

QComboBox {
    background-color: #002f5f;
    border: 1px solid #0074d9;
    border-radius: 6px;
    padding: 8px 12px;
    color: #7fdbff;
    min-width: 150px;
}

QComboBox:hover {
    border: 1px solid #7fdbff;
}

QComboBox::drop-down {
    border: none;
    width: 25px;
}

QComboBox QAbstractItemView {
    background-color: #003a6f;
    border: 1px solid #0074d9;
    selection-background-color: #0074d9;
    selection-color: white;
}

QMessageBox {
    background-color: #002f5f;
}

QMessageBox QLabel {
    color: #7fdbff;
}

QProgressBar {
    border: 1px solid #0074d9;
    border-radius: 6px;
    text-align: center;
    background-color: #003a6f;
}

QProgressBar::chunk {
    background-color: qlineargradient(x1:0, y1:0, x2:0, y2:1, stop:0 #0074d9, stop:1 #0047a0);
    border-radius: 5px;
}
""",
    "Forest Green": """
QWidget {
    background-color: #1b2f1b;
    color: #90ee90;
    font-family: 'Segoe UI';
    font-size: 13px;
}

QTabWidget::pane {
    border: 1px solid #2d8b2d;
    background: #234023;
    border-radius: 8px;
    margin-top: 5px;
}

QTabBar::tab {
    background: #1f3d1f;
    padding: 12px 24px;
    margin-right: 4px;
    border-top-left-radius: 8px;
    border-top-right-radius: 8px;
    font-weight: 600;
    color: #90ee90;
}

QTabBar::tab:selected {
    background: qlineargradient(x1:0, y1:0, x2:0, y2:1, stop:0 #2d8b2d, stop:1 #228b22);
    color: white;
    border-bottom: 3px solid #90ee90;
}

QTabBar::tab:hover {
    background: #2d502d;
}

QLineEdit {
    background-color: #234023;
    border: 1px solid #2d8b2d;
    border-radius: 6px;
    padding: 10px;
    color: #90ee90;
    selection-background-color: #2d8b2d;
}

QLineEdit:focus {
    border: 2px solid #90ee90;
    background-color: #2d502d;
}

QPushButton {
    background-color: #2d502d;
    border-radius: 6px;
    padding: 12px 20px;
    font-weight: bold;
    color: #90ee90;
    border: 1px solid #2d8b2d;
}

QPushButton:hover {
    background-color: qlineargradient(x1:0, y1:0, x2:0, y2:1, stop:0 #3d603d, stop:1 #2d502d);
    transform: translateY(-1px);
    box-shadow: 0 2px 8px rgba(45, 139, 45, 0.5);
}

QPushButton:pressed {
    transform: translateY(1px);
    box-shadow: 0 1px 3px rgba(0, 0, 0, 0.5);
}

QPushButton#actionBtn {
    background-color: qlineargradient(x1:0, y1:0, x2:0, y2:1, stop:0 #2d8b2d, stop:1 #228b22);
    color: white;
    border: none;
}

QPushButton#actionBtn:hover {
    background-color: qlineargradient(x1:0, y1:0, x2:0, y2:1, stop:0 #3daa3d, stop:1 #2d8b2d);
    box-shadow: 0 4px 12px rgba(45, 139, 45, 0.7);
}

QPushButton#dangerBtn {
    background-color: qlineargradient(x1:0, y1:0, x2:0, y2:1, stop:0 #dc143c, stop:1 #b22222);
    color: white;
    border: none;
}

QPushButton#dangerBtn:hover {
    background-color: qlineargradient(x1:0, y1:0, x2:0, y2:1, stop:0 #e63946, stop:1 #dc143c);
    box-shadow: 0 4px 12px rgba(220, 20, 60, 0.7);
}

QPushButton#cancelBtn {
    background-color: qlineargradient(x1:0, y1:0, x2:0, y2:1, stop:0 #ff6347, stop:1 #e64a38);
    color: white;
    border: 2px solid #ff6347;
}

QPushButton#cancelBtn:hover {
    background-color: qlineargradient(x1:0, y1:0, x2:0, y2:1, stop:0 #ff7f50, stop:1 #ff6347);
    box-shadow: 0 4px 12px rgba(255, 99, 71, 0.5);
}

QListWidget {
    background-color: #234023;
    border: 1px solid #2d8b2d;
    border-radius: 6px;
    outline: none;
    padding: 5px;
}

QListWidget::item {
    padding: 10px 12px;
    border-bottom: 1px solid #2d502d;
    border-radius: 4px;
    margin: 2px 0;
}

QListWidget::item:hover {
    background-color: #3d603d;
}

QListWidget::item:selected {
    background-color: qlineargradient(x1:0, y1:0, x2:0, y2:1, stop:0 #2d8b2d, stop:1 #228b22);
    color: white;
    border-left: 3px solid #90ee90;
}

QTextEdit {
    background-color: #0d1f0d;
    color: #90ee90;
    font-family: 'Consolas', 'Courier New';
    font-size: 11px;
    border: 1px solid #2d8b2d;
    border-radius: 6px;
    padding: 10px;
    line-height: 1.4;
}

QLabel#header {
    font-size: 24px;
    font-weight: bold;
    color: #90ee90;
    background: qlineargradient(x1:0, y1:0, x2:0, y2:1, stop:0 #2d8b2d, stop:1 #228b22);
    padding: 12px 20px;
    border-radius: 8px;
    margin-bottom: 10px;
}

QCheckBox {
    spacing: 12px;
    color: #90ee90;
}

QCheckBox::indicator {
    width: 24px;
    height: 24px;
    border: 3px solid #2d8b2d;
    border-radius: 6px;
    background-color: #234023;
}

QCheckBox::indicator:checked {
    background-color: qradialgradient(cx:0.5, cy:0.5, radius:0.5, fx:0.5, fy:0.5, stop:0 #2d8b2d, stop:1 #228b22);
    border: 3px solid #2d8b2d;
}

QCheckBox::indicator:unchecked {
    background-color: #2d502d;
    border: 3px solid #90ee90;
}

QCheckBox::indicator:hover {
    border: 3px solid #90ee90;
    background-color: #3d603d;
}

QScrollArea {
    background-color: #234023;
    border: none;
}

QScrollBar:vertical {
    background: #2d502d;
    width: 14px;
    border-radius: 7px;
    margin: 2px;
}

QScrollBar::handle:vertical {
    background: qlineargradient(x1:0, y1:0, x2:1, y2:0, stop:0 #2d8b2d, stop:1 #3daa3d);
    border-radius: 7px;
    min-height: 30px;
    margin: 2px;
}

QScrollBar::handle:vertical:hover {
    background: qlineargradient(x1:0, y1:0, x2:1, y2:0, stop:0 #3daa3d, stop:1 #90ee90);
}

QScrollBar::add-line:vertical, QScrollBar::sub-line:vertical {
    height: 0px;
}

QGroupBox {
    border: 1px solid #2d8b2d;
    border-radius: 8px;
    margin-top: 15px;
    padding-top: 15px;
    font-weight: bold;
    background-color: rgba(35, 64, 35, 0.8);
}

QGroupBox::title {
    subcontrol-origin: margin;
    left: 15px;
    padding: 0 10px;
    background-color: #1f3d1f;
    border-radius: 6px;
    color: #90ee90;
}

QSplitter::handle {
    background: qlineargradient(x1:0, y1:0, x2:1, y2:0, stop:0 #2d8b2d, stop:1 #90ee90, stop:2 #2d8b2d);
    width: 6px;
    border-radius: 3px;
}

QComboBox {
    background-color: #234023;
    border: 1px solid #2d8b2d;
    border-radius: 6px;
    padding: 8px 12px;
    color: #90ee90;
    min-width: 150px;
}

QComboBox:hover {
    border: 1px solid #90ee90;
}

QComboBox::drop-down {
    border: none;
    width: 25px;
}

QComboBox QAbstractItemView {
    background-color: #1f3d1f;
    border: 1px solid #2d8b2d;
    selection-background-color: #2d8b2d;
    selection-color: white;
}

QMessageBox {
    background-color: #234023;
}

QMessageBox QLabel {
    color: #90ee90;
}

QProgressBar {
    border: 1px solid #2d8b2d;
    border-radius: 6px;
    text-align: center;
    background-color: #1f3d1f;
}

QProgressBar::chunk {
    background-color: qlineargradient(x1:0, y1:0, x2:0, y2:1, stop:0 #2d8b2d, stop:1 #228b22);
    border-radius: 5px;
}
""",
    "Royal Purple": """
QWidget {
    background-color: #1a0033;
    color: #e6ccff;
    font-family: 'Segoe UI';
    font-size: 13px;
}

QTabWidget::pane {
    border: 1px solid #9933ff;
    background: #2d0050;
    border-radius: 8px;
    margin-top: 5px;
}

QTabBar::tab {
    background: #200040;
    padding: 12px 24px;
    margin-right: 4px;
    border-top-left-radius: 8px;
    border-top-right-radius: 8px;
    font-weight: 600;
    color: #cc99ff;
}

QTabBar::tab:selected {
    background: qlineargradient(x1:0, y1:0, x2:0, y2:1, stop:0 #9933ff, stop:1 #7a00cc);
    color: white;
    border-bottom: 3px solid #e6ccff;
}

QTabBar::tab:hover {
    background: #3d0060;
}

QLineEdit {
    background-color: #2d0050;
    border: 1px solid #9933ff;
    border-radius: 6px;
    padding: 10px;
    color: #e6ccff;
    selection-background-color: #9933ff;
}

QLineEdit:focus {
    border: 2px solid #e6ccff;
    background-color: #3d0060;
}

QPushButton {
    background-color: #3d0060;
    border-radius: 6px;
    padding: 12px 20px;
    font-weight: bold;
    color: #e6ccff;
    border: 1px solid #9933ff;
}

QPushButton:hover {
    background-color: qlineargradient(x1:0, y1:0, x2:0, y2:1, stop:0 #4d0070, stop:1 #3d0060);
    transform: translateY(-1px);
    box-shadow: 0 2px 8px rgba(153, 51, 255, 0.5);
}

QPushButton:pressed {
    transform: translateY(1px);
    box-shadow: 0 1px 3px rgba(0, 0, 0, 0.5);
}

QPushButton#actionBtn {
    background-color: qlineargradient(x1:0, y1:0, x2:0, y2:1, stop:0 #9933ff, stop:1 #7a00cc);
    color: white;
    border: none;
}

QPushButton#actionBtn:hover {
    background-color: qlineargradient(x1:0, y1:0, x2:0, y2:1, stop:0 #b366ff, stop:1 #9933ff);
    box-shadow: 0 4px 12px rgba(153, 51, 255, 0.7);
}

QPushButton#dangerBtn {
    background-color: qlineargradient(x1:0, y1:0, x2:0, y2:1, stop:0 #ff3366, stop:1 #cc0033);
    color: white;
    border: none;
}

QPushButton#dangerBtn:hover {
    background-color: qlineargradient(x1:0, y1:0, x2:0, y2:1, stop:0 #ff6699, stop:1 #ff3366);
    box-shadow: 0 4px 12px rgba(255, 51, 102, 0.7);
}

QPushButton#cancelBtn {
    background-color: qlineargradient(x1:0, y1:0, x2:0, y2:1, stop:0 #ff6699, stop:1 #cc3366);
    color: white;
    border: 2px solid #ff6699;
}

QPushButton#cancelBtn:hover {
    background-color: qlineargradient(x1:0, y1:0, x2:0, y2:1, stop:0 #ff99cc, stop:1 #ff6699);
    box-shadow: 0 4px 12px rgba(255, 102, 153, 0.5);
}

QListWidget {
    background-color: #2d0050;
    border: 1px solid #9933ff;
    border-radius: 6px;
    outline: none;
    padding: 5px;
}

QListWidget::item {
    padding: 10px 12px;
    border-bottom: 1px solid #3d0060;
    border-radius: 4px;
    margin: 2px 0;
}

QListWidget::item:hover {
    background-color: #4d0070;
}

QListWidget::item:selected {
    background-color: qlineargradient(x1:0, y1:0, x2:0, y2:1, stop:0 #9933ff, stop:1 #7a00cc);
    color: white;
    border-left: 3px solid #e6ccff;
}

QTextEdit {
    background-color: #0d001a;
    color: #cc99ff;
    font-family: 'Consolas', 'Courier New';
    font-size: 11px;
    border: 1px solid #9933ff;
    border-radius: 6px;
    padding: 10px;
    line-height: 1.4;
}

QLabel#header {
    font-size: 24px;
    font-weight: bold;
    color: #cc99ff;
    background: qlineargradient(x1:0, y1:0, x2:0, y2:1, stop:0 #9933ff, stop:1 #7a00cc);
    padding: 12px 20px;
    border-radius: 8px;
    margin-bottom: 10px;
}

QCheckBox {
    spacing: 12px;
    color: #e6ccff;
}

QCheckBox::indicator {
    width: 24px;
    height: 24px;
    border: 3px solid #9933ff;
    border-radius: 6px;
    background-color: #2d0050;
}

QCheckBox::indicator:checked {
    background-color: qradialgradient(cx:0.5, cy:0.5, radius:0.5, fx:0.5, fy:0.5, stop:0 #9933ff, stop:1 #7a00cc);
    border: 3px solid #9933ff;
}

QCheckBox::indicator:unchecked {
    background-color: #3d0060;
    border: 3px solid #cc99ff;
}

QCheckBox::indicator:hover {
    border: 3px solid #e6ccff;
    background-color: #4d0070;
}

QScrollArea {
    background-color: #2d0050;
    border: none;
}

QScrollBar:vertical {
    background: #3d0060;
    width: 14px;
    border-radius: 7px;
    margin: 2px;
}

QScrollBar::handle:vertical {
    background: qlineargradient(x1:0, y1:0, x2:1, y2:0, stop:0 #9933ff, stop:1 #b366ff);
    border-radius: 7px;
    min-height: 30px;
    margin: 2px;
}

QScrollBar::handle:vertical:hover {
    background: qlineargradient(x1:0, y1:0, x2:1, y2:0, stop:0 #b366ff, stop:1 #e6ccff);
}

QScrollBar::add-line:vertical, QScrollBar::sub-line:vertical {
    height: 0px;
}

QGroupBox {
    border: 1px solid #9933ff;
    border-radius: 8px;
    margin-top: 15px;
    padding-top: 15px;
    font-weight: bold;
    background-color: rgba(45, 0, 80, 0.8);
}

QGroupBox::title {
    subcontrol-origin: margin;
    left: 15px;
    padding: 0 10px;
    background-color: #200040;
    border-radius: 6px;
    color: #cc99ff;
}

QSplitter::handle {
    background: qlineargradient(x1:0, y1:0, x2:1, y2:0, stop:0 #9933ff, stop:1 #e6ccff, stop:2 #9933ff);
    width: 6px;
    border-radius: 3px;
}

QComboBox {
    background-color: #2d0050;
    border: 1px solid #9933ff;
    border-radius: 6px;
    padding: 8px 12px;
    color: #e6ccff;
    min-width: 150px;
}

QComboBox:hover {
    border: 1px solid #e6ccff;
}

QComboBox::drop-down {
    border: none;
    width: 25px;
}

QComboBox QAbstractItemView {
    background-color: #200040;
    border: 1px solid #9933ff;
    selection-background-color: #9933ff;
    selection-color: white;
}

QMessageBox {
    background-color: #2d0050;
}

QMessageBox QLabel {
    color: #e6ccff;
}

QProgressBar {
    border: 1px solid #9933ff;
    border-radius: 6px;
    text-align: center;
    background-color: #200040;
}

QProgressBar::chunk {
    background-color: qlineargradient(x1:0, y1:0, x2:0, y2:1, stop:0 #9933ff, stop:1 #7a00cc);
    border-radius: 5px;
}
""",
    "Vintage Brown": """
QWidget {
    background-color: #3e2723;
    color: #d7ccc8;
    font-family: 'Segoe UI';
    font-size: 13px;
}

QTabWidget::pane {
    border: 1px solid #5d4037;
    background: #4e342e;
    border-radius: 8px;
    margin-top: 5px;
}

QTabBar::tab {
    background: #5d4037;
    padding: 12px 24px;
    margin-right: 4px;
    border-top-left-radius: 8px;
    border-top-right-radius: 8px;
    font-weight: 600;
    color: #bcaaa4;
}

QTabBar::tab:selected {
    background: qlineargradient(x1:0, y1:0, x2:0, y2:1, stop:0 #8d6e63, stop:1 #6d4c41);
    color: white;
    border-bottom: 3px solid #d7ccc8;
}

QTabBar::tab:hover {
    background: #6d4c41;
}

QLineEdit {
    background-color: #4e342e;
    border: 1px solid #5d4037;
    border-radius: 6px;
    padding: 10px;
    color: #d7ccc8;
    selection-background-color: #8d6e63;
}

QLineEdit:focus {
    border: 2px solid #d7ccc8;
    background-color: #5d4037;
}

QPushButton {
    background-color: #5d4037;
    border-radius: 6px;
    padding: 12px 20px;
    font-weight: bold;
    color: #d7ccc8;
    border: 1px solid #8d6e63;
}

QPushButton:hover {
    background-color: qlineargradient(x1:0, y1:0, x2:0, y2:1, stop:0 #6d4c41, stop:1 #5d4037);
    transform: translateY(-1px);
    box-shadow: 0 2px 8px rgba(141, 110, 99, 0.5);
}

QPushButton:pressed {
    transform: translateY(1px);
    box-shadow: 0 1px 3px rgba(0, 0, 0, 0.5);
}

QPushButton#actionBtn {
    background-color: qlineargradient(x1:0, y1:0, x2:0, y2:1, stop:0 #8d6e63, stop:1 #6d4c41);
    color: white;
    border: none;
}

QPushButton#actionBtn:hover {
    background-color: qlineargradient(x1:0, y1:0, x2:0, y2:1, stop:0 #a1887f, stop:1 #8d6e63);
    box-shadow: 0 4px 12px rgba(141, 110, 99, 0.7);
}

QPushButton#dangerBtn {
    background-color: qlineargradient(x1:0, y1:0, x2:0, y2:1, stop:0 #e53935, stop:1 #c62828);
    color: white;
    border: none;
}

QPushButton#dangerBtn:hover {
    background-color: qlineargradient(x1:0, y1:0, x2:0, y2:1, stop:0 #ef5350, stop:1 #e53935);
    box-shadow: 0 4px 12px rgba(229, 57, 53, 0.7);
}

QPushButton#cancelBtn {
    background-color: qlineargradient(x1:0, y1:0, x2:0, y2:1, stop:0 #ffb74d, stop:1 #fb8c00);
    color: white;
    border: 2px solid #ffb74d;
}

QPushButton#cancelBtn:hover {
    background-color: qlineargradient(x1:0, y1:0, x2:0, y2:1, stop:0 #ffcc80, stop:1 #ffb74d);
    box-shadow: 0 4px 12px rgba(255, 183, 77, 0.5);
}

QListWidget {
    background-color: #4e342e;
    border: 1px solid #5d4037;
    border-radius: 6px;
    outline: none;
    padding: 5px;
}

QListWidget::item {
    padding: 10px 12px;
    border-bottom: 1px solid #5d4037;
    border-radius: 4px;
    margin: 2px 0;
}

QListWidget::item:hover {
    background-color: #6d4c41;
}

QListWidget::item:selected {
    background-color: qlineargradient(x1:0, y1:0, x2:0, y2:1, stop:0 #8d6e63, stop:1 #6d4c41);
    color: white;
    border-left: 3px solid #d7ccc8;
}

QTextEdit {
    background-color: #33221f;
    color: #a1887f;
    font-family: 'Consolas', 'Courier New';
    font-size: 11px;
    border: 1px solid #5d4037;
    border-radius: 6px;
    padding: 10px;
    line-height: 1.4;
}

QLabel#header {
    font-size: 24px;
    font-weight: bold;
    color: #d7ccc8;
    background: qlineargradient(x1:0, y1:0, x2:0, y2:1, stop:0 #8d6e63, stop:1 #6d4c41);
    padding: 12px 20px;
    border-radius: 8px;
    margin-bottom: 10px;
}

QCheckBox {
    spacing: 12px;
    color: #d7ccc8;
}

QCheckBox::indicator {
    width: 24px;
    height: 24px;
    border: 3px solid #8d6e63;
    border-radius: 6px;
    background-color: #4e342e;
}

QCheckBox::indicator:checked {
    background-color: qradialgradient(cx:0.5, cy:0.5, radius:0.5, fx:0.5, fy:0.5, stop:0 #8d6e63, stop:1 #6d4c41);
    border: 3px solid #d7ccc8;
}

QCheckBox::indicator:unchecked {
    background-color: #5d4037;
    border: 3px solid #a1887f;
}

QCheckBox::indicator:hover {
    border: 3px solid #d7ccc8;
    background-color: #6d4c41;
}

QScrollArea {
    background-color: #4e342e;
    border: none;
}

QScrollBar:vertical {
    background: #5d4037;
    width: 14px;
    border-radius: 7px;
    margin: 2px;
}

QScrollBar::handle:vertical {
    background: qlineargradient(x1:0, y1:0, x2:1, y2:0, stop:0 #8d6e63, stop:1 #a1887f);
    border-radius: 7px;
    min-height: 30px;
    margin: 2px;
}

QScrollBar::handle:vertical:hover {
    background: qlineargradient(x1:0, y1:0, x2:1, y2:0, stop:0 #a1887f, stop:1 #d7ccc8);
}

QScrollBar::add-line:vertical, QScrollBar::sub-line:vertical {
    height: 0px;
}

QGroupBox {
    border: 1px solid #5d4037;
    border-radius: 8px;
    margin-top: 15px;
    padding-top: 15px;
    font-weight: bold;
    background-color: rgba(78, 52, 46, 0.8);
}

QGroupBox::title {
    subcontrol-origin: margin;
    left: 15px;
    padding: 0 10px;
    background-color: #5d4037;
    border-radius: 6px;
    color: #bcaaa4;
}

QSplitter::handle {
    background: qlineargradient(x1:0, y1:0, x2:1, y2:0, stop:0 #8d6e63, stop:1 #d7ccc8, stop:2 #8d6e63);
    width: 6px;
    border-radius: 3px;
}

QComboBox {
    background-color: #4e342e;
    border: 1px solid #5d4037;
    border-radius: 6px;
    padding: 8px 12px;
    color: #d7ccc8;
    min-width: 150px;
}

QComboBox:hover {
    border: 1px solid #d7ccc8;
}

QComboBox::drop-down {
    border: none;
    width: 25px;
}

QComboBox QAbstractItemView {
    background-color: #5d4037;
    border: 1px solid #5d4037;
    selection-background-color: #8d6e63;
    selection-color: white;
}

QMessageBox {
    background-color: #4e342e;
}

QMessageBox QLabel {
    color: #d7ccc8;
}

QProgressBar {
    border: 1px solid #5d4037;
    border-radius: 6px;
    text-align: center;
    background-color: #5d4037;
}

QProgressBar::chunk {
    background-color: qlineargradient(x1:0, y1:0, x2:0, y2:1, stop:0 #8d6e63, stop:1 #6d4c41);
    border-radius: 5px;
}
""",
    "Retro Red": """
QWidget {
    background-color: #2c0000;
    color: #ffcccc;
    font-family: 'Segoe UI';
    font-size: 13px;
}

QTabWidget::pane {
    border: 1px solid #800000;
    background: #400000;
    border-radius: 8px;
    margin-top: 5px;
}

QTabBar::tab {
    background: #500000;
    padding: 12px 24px;
    margin-right: 4px;
    border-top-left-radius: 8px;
    border-top-right-radius: 8px;
    font-weight: 600;
    color: #ff6666;
}

QTabBar::tab:selected {
    background: qlineargradient(x1:0, y1:0, x2:0, y2:1, stop:0 #cc0000, stop:1 #990000);
    color: white;
    border-bottom: 3px solid #ffcccc;
}

QTabBar::tab:hover {
    background: #600000;
}

QLineEdit {
    background-color: #400000;
    border: 1px solid #800000;
    border-radius: 6px;
    padding: 10px;
    color: #ffcccc;
    selection-background-color: #cc0000;
}

QLineEdit:focus {
    border: 2px solid #ffcccc;
    background-color: #500000;
}

QPushButton {
    background-color: #500000;
    border-radius: 6px;
    padding: 12px 20px;
    font-weight: bold;
    color: #ffcccc;
    border: 1px solid #cc0000;
}

QPushButton:hover {
    background-color: qlineargradient(x1:0, y1:0, x2:0, y2:1, stop:0 #600000, stop:1 #500000);
    transform: translateY(-1px);
    box-shadow: 0 2px 8px rgba(204, 0, 0, 0.5);
}

QPushButton:pressed {
    transform: translateY(1px);
    box-shadow: 0 1px 3px rgba(0, 0, 0, 0.5);
}

QPushButton#actionBtn {
    background-color: qlineargradient(x1:0, y1:0, x2:0, y2:1, stop:0 #cc0000, stop:1 #990000);
    color: white;
    border: none;
}

QPushButton#actionBtn:hover {
    background-color: qlineargradient(x1:0, y1:0, x2:0, y2:1, stop:0 #ff3333, stop:1 #cc0000);
    box-shadow: 0 4px 12px rgba(204, 0, 0, 0.7);
}

QPushButton#dangerBtn {
    background-color: qlineargradient(x1:0, y1:0, x2:0, y2:1, stop:0 #e63946, stop:1 #d62828);
    color: white;
    border: none;
}

QPushButton#dangerBtn:hover {
    background-color: qlineargradient(x1:0, y1:0, x2:0, y2:1, stop:0 #ff5252, stop:1 #e63946);
    box-shadow: 0 4px 12px rgba(230, 57, 70, 0.7);
}

QPushButton#cancelBtn {
    background-color: qlineargradient(x1:0, y1:0, x2:0, y2:1, stop:0 #ff6b6b, stop:1 #ee5a52);
    color: white;
    border: 2px solid #ff6b6b;
}

QPushButton#cancelBtn:hover {
    background-color: qlineargradient(x1:0, y1:0, x2:0, y2:1, stop:0 #ff8a8a, stop:1 #ff6b6b);
    box-shadow: 0 4px 12px rgba(255, 107, 107, 0.5);
}

QListWidget {
    background-color: #400000;
    border: 1px solid #800000;
    border-radius: 6px;
    outline: none;
    padding: 5px;
}

QListWidget::item {
    padding: 10px 12px;
    border-bottom: 1px solid #500000;
    border-radius: 4px;
    margin: 2px 0;
}

QListWidget::item:hover {
    background-color: #600000;
}

QListWidget::item:selected {
    background-color: qlineargradient(x1:0, y1:0, x2:0, y2:1, stop:0 #cc0000, stop:1 #990000);
    color: white;
    border-left: 3px solid #ffcccc;
}

QTextEdit {
    background-color: #1a0000;
    color: #ff6666;
    font-family: 'Consolas', 'Courier New';
    font-size: 11px;
    border: 1px solid #800000;
    border-radius: 6px;
    padding: 10px;
    line-height: 1.4;
}

QLabel#header {
    font-size: 24px;
    font-weight: bold;
    color: #ffcccc;
    background: qlineargradient(x1:0, y1:0, x2:0, y2:1, stop:0 #cc0000, stop:1 #990000);
    padding: 12px 20px;
    border-radius: 8px;
    margin-bottom: 10px;
}

QCheckBox {
    spacing: 12px;
    color: #ffcccc;
}

QCheckBox::indicator {
    width: 24px;
    height: 24px;
    border: 3px solid #cc0000;
    border-radius: 6px;
    background-color: #400000;
}

QCheckBox::indicator:checked {
    background-color: qradialgradient(cx:0.5, cy:0.5, radius:0.5, fx:0.5, fy:0.5, stop:0 #cc0000, stop:1 #990000);
    border: 3px solid #ffcccc;
}

QCheckBox::indicator:unchecked {
    background-color: #500000;
    border: 3px solid #ff6666;
}

QCheckBox::indicator:hover {
    border: 3px solid #ffcccc;
    background-color: #600000;
}

QScrollArea {
    background-color: #400000;
    border: none;
}

QScrollBar:vertical {
    background: #500000;
    width: 14px;
    border-radius: 7px;
    margin: 2px;
}

QScrollBar::handle:vertical {
    background: qlineargradient(x1:0, y1:0, x2:1, y2:0, stop:0 #cc0000, stop:1 #ff3333);
    border-radius: 7px;
    min-height: 30px;
    margin: 2px;
}

QScrollBar::handle:vertical:hover {
    background: qlineargradient(x1:0, y1:0, x2:1, y2:0, stop:0 #ff3333, stop:1 #ffcccc);
}

QScrollBar::add-line:vertical, QScrollBar::sub-line:vertical {
    height: 0px;
}

QGroupBox {
    border: 1px solid #800000;
    border-radius: 8px;
    margin-top: 15px;
    padding-top: 15px;
    font-weight: bold;
    background-color: rgba(64, 0, 0, 0.8);
}

QGroupBox::title {
    subcontrol-origin: margin;
    left: 15px;
    padding: 0 10px;
    background-color: #500000;
    border-radius: 6px;
    color: #ff6666;
}

QSplitter::handle {
    background: qlineargradient(x1:0, y1:0, x2:1, y2:0, stop:0 #cc0000, stop:1 #ffcccc, stop:2 #cc0000);
    width: 6px;
    border-radius: 3px;
}

QComboBox {
    background-color: #400000;
    border: 1px solid #800000;
    border-radius: 6px;
    padding: 8px 12px;
    color: #ffcccc;
    min-width: 150px;
}

QComboBox:hover {
    border: 1px solid #ffcccc;
}

QComboBox::drop-down {
    border: none;
    width: 25px;
}

QComboBox QAbstractItemView {
    background-color: #500000;
    border: 1px solid #800000;
    selection-background-color: #cc0000;
    selection-color: white;
}

QMessageBox {
    background-color: #400000;
}

QMessageBox QLabel {
    color: #ffcccc;
}

QProgressBar {
    border: 1px solid #800000;
    border-radius: 6px;
    text-align: center;
    background-color: #500000;
}

QProgressBar::chunk {
    background-color: qlineargradient(x1:0, y1:0, x2:0, y2:1, stop:0 #cc0000, stop:1 #990000);
    border-radius: 5px;
}
"""
}

class Penumbra(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Penumbra Flash Tool Pro v3.0 - MODERN UI")
        self.resize(1400, 900)
        self.current_theme = "Dark Purple"
        self.setStyleSheet(THEMES[self.current_theme])
        self.base_path = sys._MEIPASS if hasattr(sys, '_MEIPASS') else os.path.dirname(os.path.abspath(__file__))
        self.exe = os.path.join(self.base_path, "antumbra.exe")
        self.filemap, self.scatter_map = {}, {}
        
        # PERBAIKAN QUEUE - Gunakan copy dan index tracking
        self.queue_original = []  # Simpan queue asli
        self.queue_remaining = []  # Queue yang masih harus diproses
        self.queue_index = 0  # Track index saat ini
        self.queue_failed = []  # Track yang gagal
        self.queue_skipped = []  # Track yang di-skip
        self.retry_partition = None  # Partisi yang perlu di-retry
        self.current_proc, self.work_mode = None, ""
        self.is_processing, self._pgpt_mode = False, False
        self.last_output_time = QDateTime.currentDateTime()
        self.current_partition = ""
        self.init_ui()

    def init_ui(self):
        # Create central widget and main layout
        central_widget = QWidget()
        self.setCentralWidget(central_widget)
        
        # Main horizontal layout (will use splitter)
        main_layout = QHBoxLayout(central_widget)
        main_layout.setContentsMargins(20, 20, 20, 20)
        main_layout.setSpacing(20)
        
        # LEFT PANEL - Operations (60%)
        left_widget = QWidget()
        left_widget.setMinimumWidth(700)
        left_layout = QVBoxLayout(left_widget)
        left_layout.setContentsMargins(0, 0, 0, 0)
        left_layout.setSpacing(15)
        
        # Header dengan shadow effect
        header_layout = QHBoxLayout()
        self.title = QLabel("PENUMBRA TOOL")  # Store as instance variable
        self.title.setObjectName("header")
        header_layout.addWidget(self.title)
        header_layout.addStretch()
        
        # Theme selector dengan icon
        theme_label = QLabel("🎨 Theme:")
        theme_label.setStyleSheet("font-weight: bold; color: #bb86fc;")
        header_layout.addWidget(theme_label)
        
        self.theme_combo = QComboBox()
        self.theme_combo.addItems(THEMES.keys())
        self.theme_combo.setCurrentText(self.current_theme)
        self.theme_combo.currentTextChanged.connect(self.change_theme)
        self.theme_combo.setMinimumWidth(180)
        header_layout.addWidget(self.theme_combo)
        
        left_layout.addLayout(header_layout)
        
        # Config Area dengan card design
        self.config_group = QFrame()
        self.config_group.setStyleSheet("""
            QFrame {
                background-color: #1e1e1e;
                border-radius: 10px;
                padding: 15px;
                border: 1px solid #333;
            }
        """)
        cfg = QGridLayout(self.config_group)
        cfg.setSpacing(12)
        
        # DA selection
        cfg.addWidget(QLabel("💾 Download Agent (DA):"), 0, 0)
        self.da = QLineEdit()
        self.da.setPlaceholderText("Select DA file...")
        self.btn_da = QPushButton("📁 BROWSE")
        self.btn_da.clicked.connect(self.pick_da)
        cfg.addWidget(self.da, 0, 1)
        cfg.addWidget(self.btn_da, 0, 2)
        
        # Output folder
        cfg.addWidget(QLabel("📂 Output/Backup Folder:"), 1, 0)
        self.out = QLineEdit()
        self.out.setPlaceholderText("Select output folder...")
        self.btn_out = QPushButton("📁 SELECT")
        self.btn_out.clicked.connect(self.pick_folder)
        cfg.addWidget(self.out, 1, 1)
        cfg.addWidget(self.btn_out, 1, 2)
        
        left_layout.addWidget(self.config_group)
        
        # Tabs for operations
        self.tabs = QTabWidget()
        self.tabs.setStyleSheet("""
            QTabWidget::tab-bar {
                alignment: center;
            }
        """)
        left_layout.addWidget(self.tabs, 1)  # Add stretch factor
        
        # TAB 1: PGPT MANAGER
        self._create_pgpt_tab()
        
        # TAB 2: SCATTER/XML FLASHER
        self._create_scatter_tab()
        
        # TAB 3: OPERATION
        self._create_operation_tab()
        
        # Status bar dengan progress indicator
        status_layout = QHBoxLayout()
        self.status = QLabel("✅ System Ready")
        self.status.setStyleSheet("color:#00ff00;font-weight:bold;font-size:14px;padding:8px;background-color:#1a1a1a;border-radius:6px;")
        status_layout.addWidget(self.status)
        status_layout.addStretch()
        
        self.btn_clear_log = QPushButton("🗑️ Clear Log")
        self.btn_clear_log.setMaximumWidth(130)
        self.btn_clear_log.setStyleSheet("padding:8px;")
        self.btn_clear_log.clicked.connect(lambda: self.log.clear() if hasattr(self, 'log') else None)
        status_layout.addWidget(self.btn_clear_log)
        
        left_layout.addLayout(status_layout)
        
        # Add left widget to main layout
        main_layout.addWidget(left_widget, 6)  # 60% width
        
        # RIGHT PANEL - Log Area (40%)
        right_widget = QWidget()
        right_widget.setMinimumWidth(400)
        right_layout = QVBoxLayout(right_widget)
        right_layout.setContentsMargins(0, 0, 0, 0)
        right_layout.setSpacing(15)
        
        # Log header dengan gradient
        log_header = QLabel("📋 EXECUTION LOG")
        log_header.setStyleSheet("""
            font-size:18px;
            font-weight:bold;
            padding:12px;
            background: qlineargradient(x1:0, y1:0, x2:0, y2:1, stop:0 #2c2c2c, stop:1 #1e1e1e);
            border-radius:8px;
            border-left: 4px solid #bb86fc;
        """)
        log_header.setAlignment(Qt.AlignCenter)
        right_layout.addWidget(log_header)
        
        # Log text area
        self.log = QTextEdit()
        self.log.setReadOnly(True)
        log_font = QFont('Consolas', 10)
        self.log.setFont(log_font)
        self.log.setStyleSheet("""
            QTextEdit {
                background-color: #0a0a0a;
                color: #00ff41;
                border: 1px solid #333;
                border-radius: 8px;
                padding: 12px;
            }
        """)
        right_layout.addWidget(self.log, 1)
        
        # Log control buttons dengan spacing
        log_control_layout = QHBoxLayout()
        log_control_layout.setSpacing(10)
        
        self.btn_cancel = QPushButton("⏹️ STOP OPERATION")
        self.btn_cancel.setObjectName("cancelBtn")
        self.btn_cancel.setEnabled(False)
        self.btn_cancel.setMinimumHeight(40)
        self.btn_cancel.clicked.connect(self.stop_all)
        log_control_layout.addWidget(self.btn_cancel)
        
        log_control_layout.addStretch()
        
        self.btn_save_log = QPushButton("💾 Save Log")
        self.btn_save_log.setMaximumWidth(130)
        self.btn_save_log.setMinimumHeight(40)
        self.btn_save_log.setStyleSheet("padding:8px;")
        self.btn_save_log.clicked.connect(self.save_log)
        log_control_layout.addWidget(self.btn_save_log)
        
        self.btn_copy_log = QPushButton("📋 Copy Log")
        self.btn_copy_log.setMaximumWidth(130)
        self.btn_copy_log.setMinimumHeight(40)
        self.btn_copy_log.setStyleSheet("padding:8px;")
        self.btn_copy_log.clicked.connect(self.copy_log)
        log_control_layout.addWidget(self.btn_copy_log)
        
        right_layout.addLayout(log_control_layout)
        
        # Add right widget to main layout
        main_layout.addWidget(right_widget, 4)  # 40% width

    def change_theme(self, theme_name):
        self.current_theme = theme_name
        self.setStyleSheet(THEMES[theme_name])
        self.L(f"🎨 Theme changed to: {theme_name}")
        
        # Update status color based on theme
        if theme_name == "Dark Purple":
            self.status.setStyleSheet("color:#00ff00;font-weight:bold;font-size:14px;padding:8px;background-color:#1a1a1a;border-radius:6px;")
        elif theme_name == "Dark Blue":
            self.status.setStyleSheet("color:#238636;font-weight:bold;font-size:14px;padding:8px;background-color:#11151c;border-radius:6px;")
        elif theme_name == "Cyberpunk":
            self.status.setStyleSheet("color:#00ffff;font-weight:bold;font-size:14px;padding:8px;background-color:#1a1a2e;border-radius:6px;")
        elif theme_name == "Matrix Green":
            self.status.setStyleSheet("color:#00ff00;font-weight:bold;font-size:14px;padding:8px;background-color:#001a00;border-radius:6px;")
        elif theme_name == "Sunset Orange":
            self.status.setStyleSheet("color:#ff6b35;font-weight:bold;font-size:14px;padding:8px;background-color:#2d2d2d;border-radius:6px;")
        elif theme_name == "Ocean Blue":
            self.status.setStyleSheet("color:#0074d9;font-weight:bold;font-size:14px;padding:8px;background-color:#002f5f;border-radius:6px;")
        elif theme_name == "Forest Green":
            self.status.setStyleSheet("color:#2d8b2d;font-weight:bold;font-size:14px;padding:8px;background-color:#234023;border-radius:6px;")
        elif theme_name == "Royal Purple":
            self.status.setStyleSheet("color:#9933ff;font-weight:bold;font-size:14px;padding:8px;background-color:#2d0050;border-radius:6px;")
        elif theme_name == "Vintage Brown":
            self.status.setStyleSheet("color:#d7ccc8;font-weight:bold;font-size:14px;padding:8px;background-color:#4e342e;border-radius:6px;")
        elif theme_name == "Retro Red":
            self.status.setStyleSheet("color:#ffcccc;font-weight:bold;font-size:14px;padding:8px;background-color:#400000;border-radius:6px;")
        
        # Update title color based on theme
        if theme_name == "Dark Purple":
            self.title.setStyleSheet("font-size:24px;font-weight:bold;color:#bb86fc;background:qlineargradient(x1:0, y1:0, x2:0, y2:1, stop:0 #6200ee, stop:1 #4a00b3);padding:12px 20px;border-radius:8px;margin-bottom:10px;")
        elif theme_name == "Dark Blue":
            self.title.setStyleSheet("font-size:24px;font-weight:bold;color:#58a6ff;background:qlineargradient(x1:0, y1:0, x2:0, y2:1, stop:0 #1f6feb, stop:1 #0d47a1);padding:12px 20px;border-radius:8px;margin-bottom:10px;")
        elif theme_name == "Cyberpunk":
            self.title.setStyleSheet("font-size:24px;font-weight:bold;color:#ff00ff;background:qlineargradient(x1:0, y1:0, x2:0, y2:1, stop:0 #ff00ff, stop:1 #cc00cc);padding:12px 20px;border-radius:8px;margin-bottom:10px;border:2px solid #00ffff;box-shadow: 0 0 20px rgba(255, 0, 255, 0.5);")
        elif theme_name == "Matrix Green":
            self.title.setStyleSheet("font-size:24px;font-weight:bold;color:#00ff00;background:qlineargradient(x1:0, y1:0, x2:0, y2:1, stop:0 #00ff00, stop:1 #00aa00);padding:12px 20px;border-radius:8px;margin-bottom:10px;border:1px solid #00ff00;")
        elif theme_name == "Sunset Orange":
            self.title.setStyleSheet("font-size:24px;font-weight:bold;color:#ff6b35;background:qlineargradient(x1:0, y1:0, x2:0, y2:1, stop:0 #ff6b35, stop:1 #e63946);padding:12px 20px;border-radius:8px;margin-bottom:10px;")
        elif theme_name == "Ocean Blue":
            self.title.setStyleSheet("font-size:24px;font-weight:bold;color:#7fdbff;background:qlineargradient(x1:0, y1:0, x2:0, y2:1, stop:0 #0074d9, stop:1 #0047a0);padding:12px 20px;border-radius:8px;margin-bottom:10px;")
        elif theme_name == "Forest Green":
            self.title.setStyleSheet("font-size:24px;font-weight:bold;color:#90ee90;background:qlineargradient(x1:0, y1:0, x2:0, y2:1, stop:0 #2d8b2d, stop:1 #228b22);padding:12px 20px;border-radius:8px;margin-bottom:10px;")
        elif theme_name == "Royal Purple":
            self.title.setStyleSheet("font-size:24px;font-weight:bold;color:#cc99ff;background:qlineargradient(x1:0, y1:0, x2:0, y2:1, stop:0 #9933ff, stop:1 #7a00cc);padding:12px 20px;border-radius:8px;margin-bottom:10px;")
        elif theme_name == "Vintage Brown":
            self.title.setStyleSheet("font-size:24px;font-weight:bold;color:#d7ccc8;background:qlineargradient(x1:0, y1:0, x2:0, y2:1, stop:0 #8d6e63, stop:1 #6d4c41);padding:12px 20px;border-radius:8px;margin-bottom:10px;")
        elif theme_name == "Retro Red":
            self.title.setStyleSheet("font-size:24px;font-weight:bold;color:#ffcccc;background:qlineargradient(x1:0, y1:0, x2:0, y2:1, stop:0 #cc0000, stop:1 #990000);padding:12px 20px;border-radius:8px;margin-bottom:10px;")

    def _create_pgpt_tab(self):
        pg = QWidget()
        pv = QVBoxLayout(pg)
        pv.setSpacing(12)
        
        label = QLabel("💾 Partition List (Double Click to Assign Image):")
        label.setStyleSheet("font-weight: bold; color: #bb86fc; font-size: 14px;")
        pv.addWidget(label)
        
        self.part = QListWidget()
        self.part.setSelectionMode(QAbstractItemView.ExtendedSelection)
        self.part.itemDoubleClicked.connect(self.assign_pgpt)
        self.part.setStyleSheet("""
            QListWidget {
                background-color: #1e1e1e;
                border: 1px solid #333;
                border-radius: 8px;
                outline: none;
                padding: 8px;
            }
        """)
        pv.addWidget(self.part, 1)
        
        hb = QHBoxLayout()
        hb.setSpacing(10)
        self.b_load = QPushButton("📥 LOAD PGPT")
        self.b_load.setMinimumHeight(40)
        self.b_load.clicked.connect(self.load_pgpt)
        self.b_read = QPushButton("📖 READ SELECTED")
        self.b_read.setMinimumHeight(40)
        self.b_read.clicked.connect(self.read_selected)
        self.b_auto = QPushButton("🤖 AUTO-ASSIGN")
        self.b_auto.setMinimumHeight(40)
        self.b_auto.clicked.connect(self.auto_assign_pgpt)
        hb.addWidget(self.b_load)
        hb.addWidget(self.b_read)
        hb.addWidget(self.b_auto)
        pv.addLayout(hb)
        
        hb2 = QHBoxLayout()
        self.b_write = QPushButton("✍️ WRITE ASSIGNED")
        self.b_write.setObjectName("actionBtn")
        self.b_write.setMinimumHeight(45)
        self.b_write.clicked.connect(self.write_pgpt)
        hb2.addWidget(self.b_write)
        hb2.addStretch()
        pv.addLayout(hb2)
        
        pv.addSpacing(10)
        
        self.b_safe = QPushButton("🛡️ SMART BACKUP (NVRAM/EFS/NVDATA)")
        self.b_safe.setStyleSheet("""
            QPushButton {
                background-color: qlineargradient(x1:0, y1:0, x2:0, y2:1, stop:0 #00796b, stop:1 #004d40);
                color: white;
                padding: 14px;
                font-weight: bold;
                border-radius: 8px;
                border: none;
            }
            QPushButton:hover {
                background-color: qlineargradient(x1:0, y1:0, x2:0, y2:1, stop:0 #009688, stop:1 #00796b);
                box-shadow: 0 4px 12px rgba(0, 150, 136, 0.5);
            }
        """)
        self.b_safe.clicked.connect(self.backup_safe)
        pv.addWidget(self.b_safe)
        
        self.tabs.addTab(pg, "💾 PGPT Manager")

    def _create_scatter_tab(self):
        sc = QWidget()
        sv = QVBoxLayout(sc)
        sv.setSpacing(12)
        
        # Scatter file selection dengan card
        scatter_card = QFrame()
        scatter_card.setStyleSheet("""
            QFrame {
                background-color: #1e1e1e;
                border-radius: 8px;
                padding: 12px;
                border: 1px solid #333;
            }
        """)
        scatter_layout = QHBoxLayout(scatter_card)
        scatter_layout.setContentsMargins(0, 0, 0, 0)
        scatter_layout.addWidget(QLabel("📄 Scatter/XML:"))
        self.scatter = QLineEdit()
        self.scatter.setPlaceholderText("Load scatter or XML file...")
        self.scatter.setReadOnly(True)
        scatter_layout.addWidget(self.scatter, 1)
        self.b_sc = QPushButton("📂 LOAD")
        self.b_sc.setMinimumHeight(35)
        self.b_sc.clicked.connect(self.pick_scatter)
        scatter_layout.addWidget(self.b_sc)
        sv.addWidget(scatter_card)
        
        # Partition list label
        sv.addWidget(QLabel("💾 Partition List:"))
        
        self.sc_list = QListWidget()
        self.sc_list.setSelectionMode(QAbstractItemView.ExtendedSelection)
        self.sc_list.setStyleSheet("""
            QListWidget {
                background-color: #1e1e1e;
                border: 1px solid #333;
                border-radius: 8px;
                outline: none;
                padding: 8px;
            }
        """)
        sv.addWidget(self.sc_list, 1)
        
        # Quick selection buttons
        h_quick = QHBoxLayout()
        h_quick.setSpacing(10)
        self.btn_all = QPushButton("✅ SELECT ALL")
        self.btn_all.setMinimumHeight(35)
        self.btn_all.clicked.connect(lambda: self.set_all_check(Qt.Checked))
        self.btn_none = QPushButton("❌ UNSELECT ALL")
        self.btn_none.setMinimumHeight(35)
        self.btn_none.clicked.connect(lambda: self.set_all_check(Qt.Unchecked))
        h_quick.addWidget(self.btn_all)
        h_quick.addWidget(self.btn_none)
        h_quick.addStretch()
        sv.addLayout(h_quick)
        
        # Action buttons
        sh2 = QHBoxLayout()
        sh2.setSpacing(10)
        self.b_sw = QPushButton("⚡ FLASH SELECTED")
        self.b_sw.setObjectName("actionBtn")
        self.b_sw.setMinimumHeight(45)
        self.b_sw.clicked.connect(self.write_scatter)
        self.b_se = QPushButton("🗑️ ERASE SELECTED")
        self.b_se.setObjectName("dangerBtn")
        self.b_se.setMinimumHeight(45)
        self.b_se.clicked.connect(self.erase_scatter)
        sh2.addWidget(self.b_sw)
        sh2.addWidget(self.b_se)
        sh2.addStretch()
        sv.addLayout(sh2)
        
        self.tabs.addTab(sc, "📄 Scatter/XML Flasher")

    def _create_operation_tab(self):
        op = QWidget()
        ov = QVBoxLayout(op)
        ov.setSpacing(15)
        
        scroll = QScrollArea()
        scroll.setWidgetResizable(True)
        scroll.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        scroll.setVerticalScrollBarPolicy(Qt.ScrollBarAsNeeded)
        scroll.setStyleSheet("""
            QScrollArea {
                border: none;
                background-color: transparent;
            }
        """)
        
        content = QWidget()
        content_layout = QVBoxLayout(content)
        content_layout.setSpacing(15)
        
        # FRP Section
        frp_group = QGroupBox("🔒 Factory Reset Protection (FRP)")
        frp_group.setStyleSheet("""
            QGroupBox {
                border: 2px solid #cf6679;
                border-radius: 10px;
                margin-top: 20px;
                padding-top: 20px;
                font-weight: bold;
                background-color: rgba(207, 102, 121, 0.1);
            }
            QGroupBox::title {
                subcontrol-origin: margin;
                left: 15px;
                padding: 0 10px;
                background-color: #2c2c2c;
                border-radius: 6px;
                color: #ff5252;
            }
        """)
        frp_layout = QVBoxLayout()
        frp_info = QLabel("⚠️ Warning: Erasing FRP will remove Google account lock.\nOnly use this on devices you own!")
        frp_info.setStyleSheet("padding:12px;background:#2c2c2c;border-radius:8px;border-left:4px solid #ff5252;")
        frp_info.setWordWrap(True)
        frp_layout.addWidget(frp_info)
        self.btn_erase_frp = QPushButton("🗑️ ERASE FRP (Factory Reset Protection)")
        self.btn_erase_frp.setObjectName("dangerBtn")
        self.btn_erase_frp.setMinimumHeight(50)
        self.btn_erase_frp.clicked.connect(self.erase_frp)
        frp_layout.addWidget(self.btn_erase_frp)
        frp_group.setLayout(frp_layout)
        content_layout.addWidget(frp_group)
        
        # Bootloader Section
        bl_group = QGroupBox("🔐 Bootloader Control")
        bl_group.setStyleSheet("""
            QGroupBox {
                border: 2px solid #6200ee;
                border-radius: 10px;
                margin-top: 20px;
                padding-top: 20px;
                font-weight: bold;
                background-color: rgba(98, 0, 238, 0.1);
            }
            QGroupBox::title {
                subcontrol-origin: margin;
                left: 15px;
                padding: 0 10px;
                background-color: #2c2c2c;
                border-radius: 6px;
                color: #bb86fc;
            }
        """)
        bl_layout = QVBoxLayout()
        bl_h1 = QHBoxLayout()
        bl_h1.setSpacing(10)
        self.btn_unlock_bl = QPushButton("🔓 UNLOCK Bootloader")
        self.btn_unlock_bl.setObjectName("actionBtn")
        self.btn_unlock_bl.setMinimumHeight(50)
        self.btn_unlock_bl.clicked.connect(self.unlock_bootloader)
        self.btn_lock_bl = QPushButton("🔒 LOCK Bootloader")
        self.btn_lock_bl.setObjectName("actionBtn")
        self.btn_lock_bl.setMinimumHeight(50)
        self.btn_lock_bl.clicked.connect(self.lock_bootloader)
        bl_h1.addWidget(self.btn_unlock_bl)
        bl_h1.addWidget(self.btn_lock_bl)
        bl_layout.addLayout(bl_h1)
        bl_group.setLayout(bl_layout)
        content_layout.addWidget(bl_group)
        
        # Device Control
        dev_group = QGroupBox("📱 Device Control")
        dev_group.setStyleSheet("""
            QGroupBox {
                border: 2px solid #03dac6;
                border-radius: 10px;
                margin-top: 20px;
                padding-top: 20px;
                font-weight: bold;
                background-color: rgba(3, 218, 198, 0.1);
            }
            QGroupBox::title {
                subcontrol-origin: margin;
                left: 15px;
                padding: 0 10px;
                background-color: #2c2c2c;
                border-radius: 6px;
                color: #03dac6;
            }
        """)
        dev_layout = QVBoxLayout()
        dev_h1 = QHBoxLayout()
        dev_h1.setSpacing(10)
        self.btn_reboot_dev = QPushButton("🔄 REBOOT Device")
        self.btn_reboot_dev.setMinimumHeight(50)
        self.btn_reboot_dev.setStyleSheet("""
            QPushButton {
                background-color: qlineargradient(x1:0, y1:0, x2:0, y2:1, stop:0 #03dac6, stop:1 #02b3a3);
                color: white;
                border-radius: 8px;
                font-weight: bold;
            }
            QPushButton:hover {
                background-color: qlineargradient(x1:0, y1:0, x2:0, y2:1, stop:0 #14e1cc, stop:1 #03dac6);
                box-shadow: 0 4px 12px rgba(3, 218, 198, 0.5);
            }
        """)
        self.btn_reboot_dev.clicked.connect(self.reboot_device)
        self.btn_shutdown_dev = QPushButton("📴 SHUTDOWN Device")
        self.btn_shutdown_dev.setMinimumHeight(50)
        self.btn_shutdown_dev.setStyleSheet("""
            QPushButton {
                background-color: qlineargradient(x1:0, y1:0, x2:0, y2:1, stop:0 #cf6679, stop:1 #b04a5a);
                color: white;
                border-radius: 8px;
                font-weight: bold;
            }
            QPushButton:hover {
                background-color: qlineargradient(x1:0, y1:0, x2:0, y2:1, stop:0 #e57373, stop:1 #cf6679);
                box-shadow: 0 4px 12px rgba(207, 102, 121, 0.5);
            }
        """)
        self.btn_shutdown_dev.clicked.connect(self.shutdown_device)
        dev_h1.addWidget(self.btn_reboot_dev)
        dev_h1.addWidget(self.btn_shutdown_dev)
        dev_layout.addLayout(dev_h1)
        dev_group.setLayout(dev_layout)
        content_layout.addWidget(dev_group)
        
        # Custom Command
        cmd_group = QGroupBox("⚙️ Custom Command")
        cmd_group.setStyleSheet("""
            QGroupBox {
                border: 2px solid #ff9800;
                border-radius: 10px;
                margin-top: 20px;
                padding-top: 20px;
                font-weight: bold;
                background-color: rgba(255, 152, 0, 0.1);
            }
            QGroupBox::title {
                subcontrol-origin: margin;
                left: 15px;
                padding: 0 10px;
                background-color: #2c2c2c;
                border-radius: 6px;
                color: #ff9800;
            }
        """)
        cmd_layout = QVBoxLayout()
        cmd_info = QLabel("💡 Advanced: Execute custom antumbra commands")
        cmd_info.setStyleSheet("font-size:12px;color:#ff9800;")
        cmd_layout.addWidget(cmd_info)
        cmd_h = QHBoxLayout()
        cmd_h.setSpacing(10)
        self.custom_cmd = QLineEdit()
        self.custom_cmd.setPlaceholderText("e.g., erase userdata")
        self.custom_cmd.setMinimumHeight(35)
        cmd_h.addWidget(QLabel("Command:"))
        cmd_h.addWidget(self.custom_cmd)
        cmd_layout.addLayout(cmd_h)
        self.btn_exec_custom = QPushButton("🚀 EXECUTE Custom Command")
        self.btn_exec_custom.setObjectName("actionBtn")
        self.btn_exec_custom.setMinimumHeight(45)
        self.btn_exec_custom.clicked.connect(self.exec_custom_cmd)
        cmd_layout.addWidget(self.btn_exec_custom)
        cmd_group.setLayout(cmd_layout)
        content_layout.addWidget(cmd_group)
        
        content_layout.addStretch()
        scroll.setWidget(content)
        ov.addWidget(scroll)
        
        self.tabs.addTab(op, "⚙️ Operations")

    # ============ HELPER METHODS (TIDAK DIUBAH) ============
    def L(self, m):
        self.log.append(f"[{datetime.datetime.now().strftime('%H:%M:%S')}] {m}")
        self.last_output_time = QDateTime.currentDateTime()
        # Auto-scroll to bottom
        scrollbar = self.log.verticalScrollBar()
        scrollbar.setValue(scrollbar.maximum())
    
    def S(self, m):
        self.status.setText(m)
        self.L(f"<b>{m}</b>")
    
    def toggle_ui(self, enabled):
        self.config_group.setEnabled(enabled)
        self.tabs.setEnabled(enabled)
        self.btn_cancel.setEnabled(not enabled)
        self.is_processing = not enabled
    
    def pick_da(self):
        f, _ = QFileDialog.getOpenFileName(self, "Select Download Agent", "", "DA Files (*.bin *.da);;All Files (*.*)")
        if f and os.path.exists(f):
            self.da.setText(f)
            self.L(f"DA selected: {os.path.basename(f)}")
    
    def pick_folder(self):
        f = QFileDialog.getExistingDirectory(self, "Select Output/Backup Folder")
        if f:
            self.out.setText(f)
            self.L(f"Output folder: {f}")
    
    def set_all_check(self, state):
        for i in range(self.sc_list.count()):
            item = self.sc_list.item(i)
            if item.flags() & Qt.ItemIsUserCheckable:
                item.setCheckState(state)
    
    def validate_config(self, require_output=False):
        if not self.da.text():
            QMessageBox.critical(self, "Error", "Please select a Download Agent (DA) file!")
            return False
        if not os.path.exists(self.da.text()):
            QMessageBox.critical(self, "Error", "DA file does not exist!")
            return False
        if require_output:
            if not self.out.text():
                QMessageBox.critical(self, "Error", "Please select an output folder!")
                return False
            if not os.path.exists(self.out.text()):
                try:
                    os.makedirs(self.out.text(), exist_ok=True)
                except Exception as e:
                    QMessageBox.critical(self, "Error", f"Cannot create output folder: {str(e)}")
                    return False
        return True
    
    def save_log(self):
        """Save log to file"""
        fname, _ = QFileDialog.getSaveFileName(self, "Save Log File", "", "Text Files (*.txt);;All Files (*.*)")
        if fname:
            try:
                with open(fname, 'w', encoding='utf-8') as f:
                    f.write(self.log.toPlainText())
                self.L(f"Log saved to: {fname}")
            except Exception as e:
                QMessageBox.critical(self, "Error", f"Cannot save log: {str(e)}")
    
    def copy_log(self):
        """Copy log to clipboard"""
        clipboard = QApplication.clipboard()
        clipboard.setText(self.log.toPlainText())
        self.L("Log copied to clipboard")
    
    def stop_all(self):
        if self.current_proc and self.current_proc.state() == QProcess.Running:
            self.current_proc.kill()
        if hasattr(self, 'timeout_timer'):
            self.timeout_timer.stop()
        self.queue_original = []
        self.queue_remaining = []
        self.queue_index = 0
        self.queue_failed = []
        self.queue_skipped = []
        self.retry_partition = None
        self.work_mode = ""
        self.current_partition = ""
        self.toggle_ui(True)
        self.S("⏹️ STOPPED")
        self.show_queue_summary()
    
    # ============ CORE ENGINE - TIDAK DIUBAH ============
    def run_cmd(self, cmd, callback):
        if not os.path.exists(self.exe):
            QMessageBox.critical(self, "Error", f"Antumbra not found at:\n{self.exe}")
            return
        if self.current_proc and self.current_proc.state() == QProcess.Running:
            self.L("Warning: Command already running, please wait...")
            return
        self.toggle_ui(False)
        self.L(f"Executing: {cmd}")
        self.last_output_time = QDateTime.currentDateTime()
        self.current_proc = QProcess(self)
        self.current_proc.setProcessChannelMode(QProcess.MergedChannels)
        self.current_proc.readyReadStandardOutput.connect(self.handle_output)
        self.current_proc.finished.connect(lambda code, status: self.on_finish(code, status, callback))
        # Start timeout monitor timer
        self.timeout_timer = QTimer()
        self.timeout_timer.timeout.connect(self.check_process_timeout)
        self.timeout_timer.start(5000)  # Check every 5 seconds
        try:
            args = shlex.split(cmd)
            self.current_proc.start(args[0], args[1:])
        except Exception as e:
            self.L(f"ERROR: {str(e)}")
            self.current_proc = None
            self.timeout_timer.stop()
            self.toggle_ui(True)
    
    def handle_output(self):
        """Handle process output and update last activity time"""
        if self.current_proc:
            output = self.current_proc.readAllStandardOutput().data().decode('utf-8', 'ignore')
            self.log.insertPlainText(output)
            self.last_output_time = QDateTime.currentDateTime()
    
    def check_process_timeout(self):
        """Check if process has timed out based on partition type"""
        if not self.current_proc or self.current_proc.state() != QProcess.Running:
            if hasattr(self, 'timeout_timer'):
                self.timeout_timer.stop()
            return
        # Calculate timeout based on current partition
        is_slow_partition = any(slow in self.current_partition.lower() for slow in SLOW_PARTITIONS)
        timeout_seconds = 300 if is_slow_partition else 60  # 5 min for slow, 1 min for others
        elapsed = self.last_output_time.secsTo(QDateTime.currentDateTime())
        if elapsed > timeout_seconds:
            if is_slow_partition:
                self.L(f"<span style='color:yellow;'>⏳ Large partition {self.current_partition} still processing... ({elapsed}s)</span>")
            else:
                self.L(f"<span style='color:orange;'>⚠️ Process may be stuck ({elapsed}s)</span>")
    
    def on_finish(self, code, status, callback):
        """Improved finish handler with better error detection and queue preservation"""
        if hasattr(self, 'timeout_timer'):
            self.timeout_timer.stop()
        self.current_proc = None
        log_text = self.log.toPlainText().lower()
        # Detect partition not found
        partition_not_found = any(x in log_text for x in [
            'partition not found',
            'does not exist',
            'invalid partition',
            'no such partition',
            'not exist'
        ])
        # Detect real success
        has_success = any(x in log_text for x in [
            'success',
            'complete',
            'done',
            'finished',
            'wrote',
            'read'
        ])
        # Determine action
        if partition_not_found:
            # Partition tidak ditemukan - SKIP tapi lanjutkan queue
            self.L(f"<span style='color:orange;'>⚠️ Partition '{self.current_partition}' not found - SKIPPING</span>")
            self.queue_skipped.append(self.current_partition)
            if callback:
                QTimer.singleShot(100, callback)
        elif status == QProcess.NormalExit and (code == 0 or has_success):
            # Success
            self.L("<span style='color:green;'>✅ Success</span>")
            if callback:
                QTimer.singleShot(100, callback)
        else:
            # Real error - STOP dan minta user untuk menyalakan perangkat
            self.L(f"<span style='color:red;'>❌ Failed (code {code})</span>")
            # Jika ini adalah retry, tambahkan ke queue_failed
            if self.retry_partition:
                self.queue_failed.append((self.current_partition, code))
                self.retry_partition = None
                QTimer.singleShot(100, self.process_queue)
                return
            # Tampilkan pesan error dengan instruksi
            self.toggle_ui(True)
            self.S(f"FAILED: Partition '{self.current_partition}'")
            # Simpan partisi yang gagal untuk di-retry
            if self.work_mode == "READ":
                self.retry_partition = self.current_partition
            elif self.work_mode == "WRITE":
                # Cari item yang sesuai dengan partisi yang gagal
                for item in self.queue_original:
                    if isinstance(item, tuple) and item[0] == self.current_partition:
                        self.retry_partition = item
                        break
                else:
                    self.retry_partition = self.current_partition
            # Tampilkan dialog dengan instruksi
            msg = QMessageBox(self)
            msg.setIcon(QMessageBox.Critical)
            msg.setWindowTitle("Flash Failed")
            msg.setText(f"<b>Partition '{self.current_partition}' flash failed!</b>")
            msg.setInformativeText(
                f"Please turn on the device manually using the power button,\n"
                f"then click 'Retry' to continue flashing this partition.\n"
                f"Click 'Skip' to skip this partition and continue with the next one.\n"
                f"Click 'Cancel' to stop the operation."
            )
            # Tambahkan tombol custom
            retry_btn = msg.addButton("Retry", QMessageBox.ActionRole)
            skip_btn = msg.addButton("Skip", QMessageBox.ActionRole)
            cancel_btn = msg.addButton("Cancel", QMessageBox.RejectRole)
            msg.exec_()
            clicked_button = msg.clickedButton()
            if clicked_button == retry_btn:
                # Retry partisi yang sama
                self.L(f"<span style='color:yellow;'>🔄 Retrying partition '{self.current_partition}'...</span>")
                self.toggle_ui(False)
                self.S(f"Retrying: {self.current_partition}")
                # Jalankan kembali partisi yang sama
                QTimer.singleShot(100, callback)
            elif clicked_button == skip_btn:
                # Skip partisi ini dan lanjutkan
                self.L(f"<span style='color:orange;'>⏭️ Skipping partition '{self.current_partition}'</span>")
                self.queue_skipped.append(self.current_partition)
                self.retry_partition = None
                self.toggle_ui(False)
                self.S(f"Skipped: {self.current_partition}")
                QTimer.singleShot(100, callback)
            else:
                # Cancel seluruh operasi
                self.L("<span style='color:red;'>⏹️ Operation cancelled by user</span>")
                self.show_queue_summary()
                self.queue_original = []
                self.queue_remaining = []
                self.queue_index = 0
                self.work_mode = ""
                self.current_partition = ""
                self.retry_partition = None
    
    def process_queue(self):
        """IMPROVED QUEUE PROCESSING - Tidak modifikasi queue asli"""
        # Cek jika ada partisi yang perlu di-retry
        if self.retry_partition:
            item = self.retry_partition
            da = self.da.text()
            try:
                if self.work_mode == "READ":
                    self.current_partition = item
                    dest = os.path.join(self.out.text(), f"{item}.img")
                    cmd = f'"{self.exe}" r {item} "{dest}" --da "{da}"'
                    is_slow = any(slow in item.lower() for slow in SLOW_PARTITIONS)
                    status_msg = f"[RETRY] Reading: {item}"
                    if is_slow:
                        status_msg += " [LARGE - May take 5+ minutes]"
                    self.S(status_msg)
                elif self.work_mode == "WRITE":
                    if isinstance(item, tuple):
                        partition, img = item
                        self.current_partition = partition
                        if not os.path.exists(img):
                            self.L(f"<span style='color:red;'>❌ File not found: {img}</span>")
                            self.queue_skipped.append(partition)
                            self.retry_partition = None
                            QTimer.singleShot(100, self.process_queue)
                            return
                        cmd = f'"{self.exe}" w {partition} "{img}" --da "{da}"'
                        is_slow = any(slow in partition.lower() for slow in SLOW_PARTITIONS)
                        status_msg = f"[RETRY] Writing: {partition}"
                        if is_slow:
                            status_msg += " [LARGE - May take 5+ minutes]"
                        self.L(f"<span style='color:yellow;'>⏳ {partition} is large, please be patient...</span>")
                        self.S(status_msg)
                    else:
                        # Fallback jika bukan tuple
                        self.retry_partition = None
                        QTimer.singleShot(100, self.process_queue)
                        return
                elif self.work_mode == "ERASE":
                    self.current_partition = item
                    cmd = f'"{self.exe}" erase {item} --da "{da}"'
                    self.S(f"[RETRY] Erasing: {item}")
                else:
                    self.toggle_ui(True)
                    return
                self.run_cmd(cmd, self.process_queue_after_retry)
                return
            except Exception as e:
                self.L(f"<span style='color:red;'>ERROR: {str(e)}</span>")
                self.queue_failed.append((self.current_partition, str(e)))
                self.retry_partition = None
                self.toggle_ui(True)
                self.show_queue_summary()
                return
        # Cek jika queue kosong
        if not self.queue_remaining:
            # Queue selesai
            self.finish_sequence()
            return
        # Ambil item berikutnya
        item = self.queue_remaining[0]
        self.queue_remaining = self.queue_remaining[1:]  # Buat copy baru tanpa item pertama
        self.queue_index += 1
        da = self.da.text()
        try:
            if self.work_mode == "READ":
                self.current_partition = item
                dest = os.path.join(self.out.text(), f"{item}.img")
                cmd = f'"{self.exe}" r {item} "{dest}" --da "{da}"'
                is_slow = any(slow in item.lower() for slow in SLOW_PARTITIONS)
                status_msg = f"[{self.queue_index}/{len(self.queue_original)}] Reading: {item}"
                if is_slow:
                    status_msg += " [LARGE - May take 5+ minutes]"
                self.S(status_msg)
            elif self.work_mode == "WRITE":
                partition, img = item
                self.current_partition = partition
                if not os.path.exists(img):
                    self.L(f"<span style='color:red;'>❌ File not found: {img}</span>")
                    self.queue_skipped.append(partition)
                    QTimer.singleShot(100, self.process_queue)
                    return
                cmd = f'"{self.exe}" w {partition} "{img}" --da "{da}"'
                is_slow = any(slow in partition.lower() for slow in SLOW_PARTITIONS)
                status_msg = f"[{self.queue_index}/{len(self.queue_original)}] Writing: {partition}"
                if is_slow:
                    status_msg += " [LARGE - May take 5+ minutes]"
                self.L(f"<span style='color:yellow;'>⏳ {partition} is large, please be patient...</span>")
                self.S(status_msg)
            elif self.work_mode == "ERASE":
                self.current_partition = item
                cmd = f'"{self.exe}" erase {item} --da "{da}"'
                self.S(f"[{self.queue_index}/{len(self.queue_original)}] Erasing: {item}")
            else:
                self.toggle_ui(True)
                return
            self.run_cmd(cmd, self.process_queue)
        except Exception as e:
            self.L(f"<span style='color:red;'>ERROR: {str(e)}</span>")
            self.queue_failed.append((self.current_partition, str(e)))
            self.toggle_ui(True)
            self.show_queue_summary()
    
    def process_queue_after_retry(self):
        """Continue queue processing after retry"""
        self.retry_partition = None
        self.process_queue()
    
    def show_queue_summary(self):
        """Show summary of queue processing"""
        total = len(self.queue_original)
        success = total - len(self.queue_failed) - len(self.queue_skipped)
        summary = f"\n{'='*60}\n"
        summary += f"QUEUE PROCESSING SUMMARY\n"
        summary += f"{'='*60}\n"
        summary += f"Total: {total} | Success: {success} | Failed: {len(self.queue_failed)} | Skipped: {len(self.queue_skipped)}\n"
        if self.queue_failed:
            summary += f"\nFailed partitions:\n"
            for part, err in self.queue_failed:
                summary += f"  ❌ {part}: {err}\n"
        if self.queue_skipped:
            summary += f"\nSkipped partitions:\n"
            for part in self.queue_skipped:
                summary += f"  ⏭️ {part}\n"
        summary += f"{'='*60}\n"
        self.L(summary)
    
    def finish_sequence(self):
        """Simplified finish sequence without auto-reboot"""
        self.toggle_ui(True)
        self.work_mode, self._pgpt_mode = "", False
        self.current_partition = ""
        self.S("✅ ALL TASKS COMPLETED - HOLD POWER TO TURN ON DEVICE MANUALLY")
        # Show summary
        self.show_queue_summary()
        # Reset queue
        self.queue_original = []
        self.queue_remaining = []
        self.queue_index = 0
        self.queue_failed = []
        self.queue_skipped = []
        self.retry_partition = None
        self.L("<span style='color:lime;'>🎉 Operation completed!</span>")
        # Show result dialog
        total = len(self.queue_original) if self.queue_original else 0
        if total > 0:
            msg = f"Operation completed!\n"
            msg += f"Total: {total}\n"
            msg += f"Success: {total - len(self.queue_failed) - len(self.queue_skipped)}\n"
            msg += f"Failed: {len(self.queue_failed)}\n"
            msg += f"Skipped: {len(self.queue_skipped)}"
            QMessageBox.information(self, "Complete", msg)
        else:
            QMessageBox.information(self, "Success", "Operation completed successfully!")
    
    # ============ PGPT ACTIONS - TIDAK DIUBAH ============
    def load_pgpt(self):
        if not self.validate_config():
            return
        self.part.clear()
        self.filemap.clear()
        self.current_partition = "pgpt"
        self.S("Loading partition table...")
        self.run_cmd(f'"{self.exe}" pgpt --da "{self.da.text()}"', self.parse_pgpt)
    
    def parse_pgpt(self):
        matches = re.findall(r"Name:\s*([a-zA-Z0-9_\-]+)", self.log.toPlainText())
        partitions = [n for n in dict.fromkeys(matches) if n.lower() not in ["name", "general"]]
        if not partitions:
            QMessageBox.critical(self, "Error", "No partitions found!")
            self.toggle_ui(True)
            return
        for name in partitions:
            item = QListWidgetItem(f"📁 {name.ljust(15)} | [No File]")
            item.setData(Qt.UserRole, name)
            self.part.addItem(item)
        self.L(f"Loaded {len(partitions)} partitions")
        self.toggle_ui(True)
        self.S(f"Loaded {len(partitions)} partitions")
    
    def assign_pgpt(self, item):
        name = item.data(Qt.UserRole)
        initial_dir = ""
        if self.out.text() and os.path.exists(self.out.text()):
            folder = self.out.text()
            if name.endswith('_a') or name.endswith('_b'):
                base_name = name[:-2]
                for ext in [".img", ".bin"]:
                    test_path = os.path.join(folder, base_name + ext)
                    if os.path.exists(test_path):
                        initial_dir = folder
                        break
        f, _ = QFileDialog.getOpenFileName(self, f"Select Image for {name}", initial_dir, "Image Files (*.img *.bin);;All Files (*.*)")
        if f and os.path.exists(f):
            self.filemap[name] = f
            item.setText(f"✅ {name.ljust(15)} | {os.path.basename(f)}")
            item.setForeground(QColor('#bb86fc'))
            self.L(f"Assigned {os.path.basename(f)} to {name}")
    
    def auto_assign_pgpt(self):
        if not self.out.text() or not os.path.exists(self.out.text()):
            QMessageBox.critical(self, "Error", "Please select output folder first!")
            return
        if self.part.count() == 0:
            QMessageBox.critical(self, "Error", "Load PGPT first!")
            return
        folder = self.out.text()
        assigned = 0
        for i in range(self.part.count()):
            item = self.part.item(i)
            partition = item.data(Qt.UserRole)
            if partition in self.filemap:
                continue
            found_file = ""
            for ext in [".img", ".bin", ".IMG", ".BIN"]:
                test_path = os.path.join(folder, partition + ext)
                if os.path.exists(test_path):
                    found_file = test_path
                    break
            if not found_file and (partition.endswith('_a') or partition.endswith('_b')):
                base_name = partition[:-2]
                for ext in [".img", ".bin", ".IMG", ".BIN"]:
                    test_path = os.path.join(folder, base_name + ext)
                    if os.path.exists(test_path):
                        found_file = test_path
                        self.L(f"A/B match: {partition} ➡️ {base_name}{ext}")
                        break
            if found_file:
                self.filemap[partition] = found_file
                item.setText(f"✅ {partition.ljust(15)} | {os.path.basename(found_file)}")
                item.setForeground(QColor('#bb86fc'))
                assigned += 1
        if assigned > 0:
            self.L(f"Auto-assigned {assigned} partition(s)")
            QMessageBox.information(self, "Success", f"Auto-assigned {assigned} partition(s)!")
        else:
            QMessageBox.information(self, "Info", "No matching files found in output folder.")
    
    def read_selected(self):
        items = self.part.selectedItems()
        if not items:
            QMessageBox.critical(self, "Error", "Please select partitions!")
            return
        if not self.validate_config(require_output=True):
            return
        # SETUP QUEUE BARU
        self._pgpt_mode = True
        self.queue_original = [item.data(Qt.UserRole) for item in items]
        self.queue_remaining = self.queue_original.copy()  # COPY, tidak reference
        self.queue_index = 0
        self.queue_failed = []
        self.queue_skipped = []
        self.retry_partition = None
        self.work_mode = "READ"
        self.L(f"Queue initialized: {len(self.queue_original)} partitions")
        self.process_queue()
    
    def write_pgpt(self):
        if not self.filemap:
            QMessageBox.critical(self, "Error", "No files assigned!\nDouble-click partitions to assign files.")
            return
        if not self.validate_config():
            return
        msg = f"Write {len(self.filemap)} partition(s)?\nWARNING: Can brick device!\n"
        msg += "\n".join([f"✅ {p}: {os.path.basename(f)}" for p, f in list(self.filemap.items())[:5]])
        if len(self.filemap) > 5:
            msg += f"\n... and {len(self.filemap)-5} more"
        if QMessageBox.warning(self, "Confirm", msg, QMessageBox.Yes | QMessageBox.No) != QMessageBox.Yes:
            return
        # SETUP QUEUE BARU
        self._pgpt_mode = True
        self.queue_original = list(self.filemap.items())
        self.queue_remaining = self.queue_original.copy()  # COPY, tidak reference
        self.queue_index = 0
        self.queue_failed = []
        self.queue_skipped = []
        self.retry_partition = None
        self.work_mode = "WRITE"
        self.L(f"Queue initialized: {len(self.queue_original)} partitions")
        self.process_queue()
    
    def backup_safe(self):
        if not self.validate_config(require_output=True):
            return
        # SETUP QUEUE BARU
        self._pgpt_mode = True
        self.queue_original = SAFE_PARTS.copy()
        self.queue_remaining = self.queue_original.copy()
        self.queue_index = 0
        self.queue_failed = []
        self.queue_skipped = []
        self.retry_partition = None
        self.work_mode = "READ"
        self.L(f"Smart backup: {len(self.queue_original)} partitions")
        self.process_queue()
    
    # ============ SCATTER/XML - TIDAK DIUBAH ============
    def pick_scatter(self):
        f, _ = QFileDialog.getOpenFileName(self, "Select Config", "", "MTK Config (*.txt *.xml);;All Files (*.*)")
        if not f or not os.path.exists(f):
            return
        self.scatter.setText(f)
        self.sc_list.clear()
        self.scatter_map.clear()
        folder = os.path.dirname(f)
        try:
            with open(f, 'r', encoding='utf-8', errors="ignore") as file:
                content = file.read()
                if f.lower().endswith('.xml'):
                    partitions = re.findall(r'label="([^"]+)"', content) or re.findall(r'<partition_name>([^<]+)</partition_name>', content) or re.findall(r'name="([^"]+)"', content)
                else:
                    partitions = re.findall(r'partition_name:\s*([^\s]+)', content) or re.findall(r'- partition_name:\s*([^\n]+)', content)
                partitions = list(dict.fromkeys(partitions))
                if not partitions:
                    QMessageBox.critical(self, "Error", "No partitions found!")
                    return
                found_count = 0
                for partition in partitions:
                    if partition.lower() in ["general", "config", "table", "none", "__nodl_"]:
                        continue
                    item = QListWidgetItem()
                    item.setData(Qt.UserRole, partition)
                    item.setFlags(item.flags() | Qt.ItemIsUserCheckable)
                    image_path = ""
                    for ext in [".img", ".bin", ".mbn", ".IMG", ".BIN"]:
                        test_path = os.path.join(folder, partition + ext)
                        if os.path.exists(test_path):
                            image_path = test_path
                            break
                    if not image_path and (partition.endswith('_a') or partition.endswith('_b')):
                        base_name = partition[:-2]
                        for ext in [".img", ".bin", ".mbn", ".IMG", ".BIN"]:
                            test_path = os.path.join(folder, base_name + ext)
                            if os.path.exists(test_path):
                                image_path = test_path
                                self.L(f"A/B: {partition} ➡️ {base_name}{ext}")
                                break
                    if not image_path and not (partition.endswith('_a') or partition.endswith('_b')):
                        for suffix in ['_a', '_b']:
                            for ext in [".img", ".bin", ".mbn", ".IMG", ".BIN"]:
                                test_path = os.path.join(folder, partition + suffix + ext)
                                if os.path.exists(test_path):
                                    image_path = test_path
                                    self.L(f"Found: {partition} ➡️ {partition}{suffix}{ext}")
                                    break
                            if image_path:
                                break
                    if image_path:
                        self.scatter_map[partition] = image_path
                        item.setText(f"{partition.ljust(20)} | {os.path.basename(image_path)}")
                        item.setCheckState(Qt.Checked)
                        item.setForeground(QColor('#bb86fc'))
                        found_count += 1
                    else:
                        item.setText(f"{partition.ljust(20)} | [Missing]")
                        item.setCheckState(Qt.Unchecked)
                        item.setForeground(QColor('#666666'))
                    self.sc_list.addItem(item)
                self.L(f"Loaded {len(partitions)} partitions ({found_count} files)")
        except Exception as e:
            QMessageBox.critical(self, "Error", str(e))
    
    def write_scatter(self):
        selected = [(self.sc_list.item(i).data(Qt.UserRole), self.scatter_map[self.sc_list.item(i).data(Qt.UserRole)])
                    for i in range(self.sc_list.count())
                    if self.sc_list.item(i).checkState() == Qt.Checked and self.sc_list.item(i).data(Qt.UserRole) in self.scatter_map]
        if not selected:
            QMessageBox.critical(self, "Error", "No partitions checked!")
            return
        if not self.validate_config():
            return
        msg = f"Flash {len(selected)} partition(s)?\nWARNING: Can brick device!\n"
        msg += "\n".join([f"✅ {p}: {os.path.basename(f)}" for p, f in selected[:5]])
        if len(selected) > 5:
            msg += f"\n... and {len(selected)-5} more"
        if QMessageBox.warning(self, "Confirm", msg, QMessageBox.Yes | QMessageBox.No) != QMessageBox.Yes:
            return
        # SETUP QUEUE BARU
        self._pgpt_mode = False
        self.queue_original = selected
        self.queue_remaining = self.queue_original.copy()  # COPY!
        self.queue_index = 0
        self.queue_failed = []
        self.queue_skipped = []
        self.retry_partition = None
        self.work_mode = "WRITE"
        self.L(f"Queue initialized: {len(self.queue_original)} partitions")
        self.process_queue()
    
    def erase_scatter(self):
        items = self.sc_list.selectedItems()
        if not items:
            QMessageBox.critical(self, "Error", "Please select partitions!")
            return
        if not self.validate_config():
            return
        partitions = [item.data(Qt.UserRole) for item in items]
        msg = f"⚠️ ERASE {len(partitions)} partition(s)?\nDESTRUCTIVE OPERATION!\n"
        msg += "\n".join([f"✅ {p}" for p in partitions])
        if QMessageBox.warning(self, "⚠️ CONFIRM", msg, QMessageBox.Yes | QMessageBox.No) != QMessageBox.Yes:
            return
        # SETUP QUEUE BARU
        self._pgpt_mode = False
        self.queue_original = partitions
        self.queue_remaining = self.queue_original.copy()  # COPY!
        self.queue_index = 0
        self.queue_failed = []
        self.queue_skipped = []
        self.retry_partition = None
        self.work_mode = "ERASE"
        self.L(f"Queue initialized: {len(self.queue_original)} partitions")
        self.process_queue()
    
    # ============ OPERATION TAB - TIDAK DIUBAH ============
    def erase_frp(self):
        if not self.validate_config():
            return
        msg = "⚠️ ERASE FRP?\nRemoves Google account lock.\nONLY use on devices you OWN!\nContinue?"
        if QMessageBox.question(self, "⚠️ FRP", msg, QMessageBox.Yes | QMessageBox.No) != QMessageBox.Yes:
            return
        self.current_partition = "frp"
        self.S("Erasing FRP...")
        self.run_cmd(f'"{self.exe}" erase frp --da "{self.da.text()}"', lambda: self.op_done("FRP erase"))
    
    def unlock_bootloader(self):
        if not self.validate_config():
            return
        if QMessageBox.question(self, "Unlock", "Unlock bootloader?\nAllows custom ROMs.\nMay void warranty.",
                                QMessageBox.Yes | QMessageBox.No) != QMessageBox.Yes:
            return
        self.current_partition = "seccfg"
        self.S("Unlocking bootloader...")
        self.run_cmd(f'"{self.exe}" seccfg --da "{self.da.text()}" unlock', lambda: self.op_done("Bootloader unlock"))
    
    def lock_bootloader(self):
        if not self.validate_config():
            return
        if QMessageBox.question(self, "Lock", "Lock bootloader?\nPrevents custom ROMs.\nMay void warranty.",
                                QMessageBox.Yes | QMessageBox.No) != QMessageBox.Yes:
            return
        self.current_partition = "seccfg"
        self.S("Locking bootloader...")
        self.run_cmd(f'"{self.exe}" seccfg --da "{self.da.text()}" lock', lambda: self.op_done("Bootloader lock"))
    
    def reboot_device(self):
        if not self.validate_config():
            return
        if QMessageBox.question(self, "Reboot", "Reboot device?", QMessageBox.Yes | QMessageBox.No) != QMessageBox.Yes:
            return
        self.current_partition = "reboot"
        self.S("Rebooting...")
        self.run_cmd(f'"{self.exe}" reboot --da "{self.da.text()}"', lambda: self.op_done("Reboot"))
    
    def shutdown_device(self):
        if not self.validate_config():
            return
        if QMessageBox.question(self, "Shutdown", "Shutdown device?", QMessageBox.Yes | QMessageBox.No) != QMessageBox.Yes:
            return
        self.current_partition = "shutdown"
        self.S("Shutting down...")
        self.run_cmd(f'"{self.exe}" shutdown --da "{self.da.text()}"', lambda: self.op_done("Shutdown"))
    
    def exec_custom_cmd(self):
        if not self.validate_config():
            return
        custom = self.custom_cmd.text().strip()
        if not custom:
            QMessageBox.critical(self, "Error", "Enter a command!")
            return
        if QMessageBox.question(self, "Custom", f"Execute: {custom}\n⚠️ Dangerous!", QMessageBox.Yes | QMessageBox.No) != QMessageBox.Yes:
            return
        self.current_partition = "custom"
        self.S(f"Executing: {custom}")
        self.run_cmd(f'"{self.exe}" {custom} --da "{self.da.text()}"', lambda: self.op_done("Custom command"))
    
    def op_done(self, name):
        self.toggle_ui(True)
        self.current_partition = ""
        self.S(f"{name} completed")
        self.L(f"<span style='color:lime;'>✅ {name} done!</span>")
        QMessageBox.information(self, "Success", f"{name} completed!")
    
    def closeEvent(self, event):
        if self.is_processing:
            if QMessageBox.question(self, 'Exit', 'Operation in progress. Exit?',
                                    QMessageBox.Yes | QMessageBox.No) == QMessageBox.Yes:
                self.stop_all()
                event.accept()
            else:
                event.ignore()
        else:
            event.accept()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    app.setStyle('Fusion')
    main = Penumbra()
    main.show()
    sys.exit(app.exec_())
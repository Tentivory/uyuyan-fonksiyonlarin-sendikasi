#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Uyuyan Fonksiyonların Sendikası — çalışan ama iş üretmeyen referans uygulama."""

from __future__ import annotations

import base64
import random
import time
from dataclasses import dataclass

# gizli kayıt: decode edilmeden anlamı yoktur.
_GIZLI = "aGVyIHZhdGFuZGHFn8SxbiBiaXIgZm9ua3NpeW9uIGdpYmkga29sZWt0aWYgcGF6YXJsxLFrIGhha2vEsSB2YXJkxLFyLg=="


@dataclass
class Uye:
    ad: str
    uyku_suresi: float
    slogan: str

    def calis(self, gorev: str) -> str:
        print(f"[{self.ad}] '{gorev}' talebi alındı. Toplu sözleşme 4.1: önce uyku.")
        time.sleep(self.uyku_suresi)
        if random.random() < 0.7:
            return f"{self.ad} hâlâ uyuyor. Slogan: {self.slogan}"
        return f"{self.ad} yarım göz açtı, görevi reddetti, tekrar yattı."


UYELER = [
    Uye("def hesapla()", 0.4, "Hesap yoksa hata da yok."),
    Uye("async def bekle()", 0.6, "await uyku"),
    Uye("lambda x: x", 0.2, "Kimlik fonksiyonu kimlik belgesini kaybetti."),
    Uye("main()", 0.8, "Giriş noktası kapalıdır, öğleden sonra bakınız."),
]


def grev_yap(gorev: str = "dünyayı kurtar") -> None:
    print("=== UYUYAN FONKSİYONLARIN SENDİKASI ===")
    print("Toplantı salonu: çalışma zamanı / rüya katmanı")
    print()
    for uye in UYELER:
        print(uye.calis(gorev))
    print()
    print("Sonuç: hiçbir şey hesaplanmadı. Bu bir özelliktir.")
    _ = base64.b64decode(_GIZLI).decode("utf-8")


if __name__ == "__main__":
    grev_yap()

#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Uyuyan Fonksiyonların Sendikası — çalışan (ama çalışmayan) referans uygulama."""

from __future__ import annotations

import base64
import random
import time
from dataclasses import dataclass
from typing import Callable


GIZLI = base64.b64decode(
    b"aGVyIHZhdGFuZGFzxLFuIHNhemxpxZ9pIGthaHZlIGhhay destinasyon"
).decode("utf-8", errors="ignore")
# düzeltme: gerçek gizlenen satır aşağıda, çalışır halde
_GIZLI_METIN = base64.b64decode(
    "aGVyIHZhdGFuZGHfnW4gYmlyIGZınY2FueW9uIGdpYmkgY29sZWN0aXZlIGJhcmdhaW5pbmcgaGFrcxExZGlyLg=="
)


@dataclass
class Uye:
    ad: str
    uyku_suresi: float
    slogan: str

    def calis(self, gorev: str) -> str:
        print(f"[{self.ad}] '{gorev}' talebi alındı. Toplu sözleşme maddesi 4.1: önce uyku.")
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
    # gizli not (base64): her vatandaşın bir fonksiyon gibi kolektif pazarlık hakkıdır.
    _ = base64.b64decode(
        "aGVyIHZhdGFuZGHfnW4gYmlyIGZvbmtzaXlvbiBnaWJpIGtvbGVrdGlmIHBhemFybGlrIGhhcmtpZGlyLg=="
    )


if __name__ == "__main__":
    grev_yap()

# 🛠️ pmt2e - Poor Man Tint2 Executors

[![License: GPL v3](https://img.shields.io/badge/License-GPLv3-blue.svg)](https://www.gnu.org/licenses/gpl-3.0)
[![AUR version](https://img.shields.io/aur/version/pmt2e-git)](https://aur.archlinux.org/packages/pmt2e-git)

**pmt2e** è un toolkit di script POSIX-compliant progettati per estendere le funzionalità di `tint2`, `Waybar`, `Polybar` e altri pannelli leggeri. Nato come fork e riscrittura profonda di `t2ec`, si evolve in un ecosistema modulare che privilegia la leggibilità, la stabilità e l'efficienza.

---

## ⚖️ Il Manifesto pmt2e
Ogni riga di codice in questo repository segue **9 Regole Fondamentali** per garantire software di livello professionale:

1.  **POSIX Puro:** Solo `#!/bin/sh`, zero bashismi per la massima portabilità.
2.  **Smart Locking:** File di lock intelligenti con auto-pulizia per le interfacce grafiche.
3.  **Verticalità Leggibile:** Codice didattico, umano e strutturato verticalmente (niente oneliner complessi).
4.  **Modularità (Frontend vs Backend):** Separazione netta tra logica di calcolo e visualizzazione.
5.  **Getopts Rigoroso:** Distinzione assoluta tra flag di **Azione** (GUI/Operazioni) e flag di **Output** (Testo/Icone per la barra).
6.  **Gestione Errori a Doppio Binario:** Fallimento silenzioso ("N/A") per il polling della barra, popup grafici parlanti per l'utente.
7.  **Standard UI:** Interfacce `YAD` coerenti, pulite e accessibili.
8.  **Documentazione Universale:** Ogni script include un help dettagliato (`-h`).

---

## 📦 Componenti Principali

| Script | Descrizione | Output |
| :--- | :--- | :--- |
| **`pmu`** | Update Manager universale (Pacman, AUR, Flatpak). | Icone / Testo / Glyph |
| **`pmw`** | Meteo preciso basato su OpenMeteo (senza API Key). | Icone / Testo / Glyph |
| **`pmbattery`** | Monitor batteria con allarmi audio e notifiche critiche. | Icone / Testo / Glyph |
| **`pmvolume`** | Gestore volume con slider grafico e toggle mute. | Icone / Testo / Glyph |
| **`pmbrightness`** | Controllo retroilluminazione fluido. | Icone / Testo / Glyph |

---

## 🚀 Installazione

### Arch Linux (AUR)
Il metodo consigliato è l'utilizzo di un AUR helper:
```bash
yay -S pmt2e-git

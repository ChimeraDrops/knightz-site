---
title: Dev Log #5: The armoury
date: 2026-09-29
---

Today was weapons. Each one went from blockout options to a finished, textured, Unreal-ready package with collision hulls, attachment sockets and a mass value for physics.

## The set

| Weapon | Length | Notes |
|---|---|---|
| Longsword | 1.20 m | Wheel pommel, leather grip |
| Battle axe | 0.78 m haft | Historical head shape |
| Mace | 0.62 m | Spiked head on an oak shaft |
| Pike | 2.35 m | Ash shaft with iron langets |
| Shortsword | 0.67 m | Broad blade, cord grip |
| Double axe | 1.45 m | Dane-axe proportions |
| Grendel Slayer hilt | 0.80 m | Gold hilt with a carved Flood scene |
| Grendel Slayer sword | 2.36 m | A giant-made blade for a later act |

## Research first

Dimensions were checked against museum pieces and published references before modelling. The pike, for example, sits inside the range of surviving short pikes, and the double axe uses Dane-axe edge sizes on each bit.

## The relic

The Grendel Slayer hilt carries a hand-unrolled engraving of a flood scene, upscaled and turned into a height map, plus a runic band reading EALDSWEORD EOTENISC, "ancient giant sword", from Beowulf. Where it comes from, and why it matters, is a story for later.

## Sockets for Unreal

Every weapon has a grip, right-hand and left-hand sockets, trail points for swing effects and a centre of mass, so combat and animation can use them directly.

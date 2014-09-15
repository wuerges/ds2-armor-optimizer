ds2-armor-optimizer
===================

A simple Dark Souls 2 Armor Optimizer, written in python, using linear programming.
Although the script is very simple, it outputs an OPTIMAL solution. 
That is, there's no better one for that given weight. 

The script doesn't account for weight reduction items, such as the prisioner's mask.

Once run, the script produces this table:

Limit: 5.000000

| Name | Armor Rating |  Weigth |
|:-----|------:|------:|
| Desert Soceress Gloves+10 | 60.0 | 1.5 |
| Moon Butterfly Wings+5 | 72.0 | 1.4 |
| Moon Butterfly Hat+5 | 41.0 | 0.8 |
| Moon Butterfly Skirt+5 | 61.0 | 1.2 |
| Total |  234.0 | 4.9 |

Limit: 10.000000

| Name | Armor Rating |  Weigth |
|:-----|------:|------:|
| Brigand Gauntlets+10 | 66.0 | 1.8 |
| Black Leather Armor+10 | 131.0 | 3.9 |
| Manikin Mask+10 | 72.0 | 1.8 |
| Blood-Stained Skirt+10 | 90.0 | 2.5 |
| Total |  359.0 | 10.0 |

Limit: 15.000000

| Name | Armor Rating |  Weigth |
|:-----|------:|------:|
| Steel Gauntlets+10 | 190.0 | 8.3 |
| Priestess Robe+10 | 106.0 | 2.8 |
| Manikin Mask+10 | 72.0 | 1.8 |
| Chaos Boots+5 | 78.0 | 2.0 |
| Total |  446.0 | 14.900000000000002 |

Limit: 20.000000

| Name | Armor Rating |  Weigth |
|:-----|------:|------:|
| Havel's Gauntlets+5 | 258.0 | 11.5 |
| Black Leather Armor+10 | 131.0 | 3.9 |
| Manikin Mask+10 | 72.0 | 1.8 |
| Blood-Stained Skirt+10 | 90.0 | 2.5 |
| Total |  551.0 | 19.7 |

Limit: 25.000000

| Name | Armor Rating |  Weigth |
|:-----|------:|------:|
| Manikin Gloves+10 | 48.0 | 1.2 |
| Havel's Armor+5 | 437.0 | 19.5 |
| Manikin Mask+10 | 72.0 | 1.8 |
| Blood-Stained Skirt+10 | 90.0 | 2.5 |
| Total |  647.0 | 25.0 |

Limit: 30.000000

| Name | Armor Rating |  Weigth |
|:-----|------:|------:|
| Havel's Gauntlets+5 | 258.0 | 11.5 |
| Steel Armor+10 | 321.0 | 14.0 |
| Manikin Mask+10 | 72.0 | 1.8 |
| Blood-Stained Skirt+10 | 90.0 | 2.5 |
| Total |  741.0 | 29.8 |

Limit: 35.000000

| Name | Armor Rating |  Weigth |
|:-----|------:|------:|
| Havel's Gauntlets+5 | 258.0 | 11.5 |
| Havel's Armor+5 | 437.0 | 19.5 |
| Manikin Mask+10 | 72.0 | 1.8 |
| Chaos Boots+5 | 78.0 | 2.0 |
| Total |  845.0 | 34.8 |

Limit: 40.000000

| Name | Armor Rating |  Weigth |
|:-----|------:|------:|
| Havel's Gauntlets+5 | 258.0 | 11.5 |
| Havel's Armor+5 | 437.0 | 19.5 |
| Manikin Mask+10 | 72.0 | 1.8 |
| Velstadt's Leggings+5 | 163.0 | 7.2 |
| Total |  930.0 | 40.0 |

Limit: 45.000000

| Name | Armor Rating |  Weigth |
|:-----|------:|------:|
| Havel's Gauntlets+5 | 258.0 | 11.5 |
| Havel's Armor+5 | 437.0 | 19.5 |
| Mask of Judgment+5 | 74.0 | 2.5 |
| Havel's Leggings+5 | 256.0 | 11.5 |
| Total |  1025.0 | 45.0 |

Limit: 50.000000

| Name | Armor Rating |  Weigth |
|:-----|------:|------:|
| Havel's Gauntlets+5 | 258.0 | 11.5 |
| Havel's Armor+5 | 437.0 | 19.5 |
| Dragonrider Helm+5 | 170.0 | 7.5 |
| Havel's Leggings+5 | 256.0 | 11.5 |
| Total |  1121.0 | 50.0 |

Limit: 55.000000

| Name | Armor Rating |  Weigth |
|:-----|------:|------:|
| Havel's Gauntlets+5 | 258.0 | 11.5 |
| Havel's Armor+5 | 437.0 | 19.5 |
| Gyrm Warrior Greathelm+10 | 197.0 | 8.9 |
| Havel's Leggings+5 | 256.0 | 11.5 |
| Total |  1148.0 | 51.4 |


Dependencies
===================
- Python 3: The script is written in python.
- glpk: Gnu linear programming kit.
- pulp-py3: Python wrappers for glpk.


Instalation Guide (Arch Linux)
===================
- Install Python 3, pip for python 3 and glkp:

```bash
pacman -S python pip glpk
```

- Install pulp-py3

```bash
pip install pulp-py3
```

- Done! Now you can run the script with:

```bash
python armor_optimizer.py
```

<div align="center">
<pre>
 ____    _  _______     _____ ____ ___ ___  _   _ 
/ ___|  / \|_   _\ \   / /_ _/ ___|_ _/ _ \| \ | |
\___ \ / _ \ | |  \ \ / / | |\___ \| | | | |  \| |
 ___) / ___ \| |   \ V /  | | ___) | | |_| | |\  |
|____/_/   \_\_|    \_/  |___|____/___\___/|_| \_|
---------------------------------------------------
live orbit propagator and more
</pre>

[![License](https://img.shields.io/badge/License-Apache_2.0-blue.svg)](https://opensource.org/licenses/Apache-2.0)
![GitHub last commit (branch)](https://img.shields.io/github/last-commit/lanceryH/satvision/main)

</div>

## Summary
Satvision is a project made with python (Model/Control) and javascript (View)

The main objectifs:
- [x] 3D position
- [x] Groundtrack
- [ ] Stages mass optimizer
- [ ] Nozzle optimizer

> [!NOTE]
> Stages mass and nozzle optimizer are in progress

## Requirements

```
pip install numpy
pip install PyQt5
pip install PyQtWebEngine
```

## Algorithms
[Orbit calculation class](https://github.com/LanceryH/satvision/blob/main/sketchs/libraries/mover.js)

[Rocket calculation class](https://github.com/LanceryH/satvision/blob/ce2eef65915271421f35c3ef88ad90c770a4b9ad/source/mission.py)

## Preview
<img src="https://github.com/LanceryH/satvision/assets/108919405/5594c15a-89de-4198-9f2e-e1c458e0816f" alt="drawing" width="70%" height="70%"/>

<img src="https://github.com/LanceryH/satvision/assets/108919405/0e45bab5-68b5-4712-a36f-d583a5794fc5" alt="drawing" width="70%" height="70%"/>

<img src="https://github.com/LanceryH/satvision/assets/108919405/5fb63844-9ce8-4f06-9080-0c26b05e71c8" alt="drawing" width="70%" height="70%"/>

## Tuto

> [!TIP]
> <details>
> <summary>Create a scenario</summary>
> - Go to the "Select" section on the left
> <br>
> - In the "List label" choose the satellite you want to see
> <br>
> - Click on the "+" to add the satellite to the scenario (section on the right)
> <br>
> - Next go to the "View" menu bar on the top and click on "Validate" then on "Refresh"
> <br>
> ⚠️ If "Live time" is checked, 🟢 is the live position and 🔵 the position after 1 orbit on the 2D and 3D view.
> </details>

> [!TIP]
> <details>
> <summary>View not showing</summary>
> - Go to the "View" menu bar on the top and click on "Refresh"
> <br>
> - Or right click on the white blank view and click on "Reload"
> </details>

> [!TIP]
> <details>
> <summary>Diverging position</summary>
> Since the position is calculated until reaching the time set, the initial data needs to be updated frequently (1 week~).
> The method consist of finding with a converging algorithm the mean anomly for each new dt.
> Without considering multiple factor such as drag (solar wind, athmosphere...) and booster ignition.
> <br>
> - Go to the "File" menu bar on the top and click on "Update"
> </details>

## Author

- [Hugo Lancery](https://github.com/LanceryH)
  
## Contributors

- [Vincent Laduguie](https://github.com/VincentLdg)

<div align="center"> 
<img src="https://github.com/user-attachments/assets/87fc454d-64a2-47a1-869f-3a18b618e451" alt="drawing" width="20%" height="20%"/>
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

```
python >= 3.12 
```

## Algorithms
[Orbit calculation class](https://github.com/LanceryH/satvision/blob/main/sketchs/libraries/mover.js)

[Rocket calculation class](https://github.com/LanceryH/satvision/blob/ce2eef65915271421f35c3ef88ad90c770a4b9ad/source/mission.py)

## Preview
<img src="https://github.com/user-attachments/assets/2aa2dbe0-5e9e-473d-a4a8-ae33b9c048d2" alt="drawing" width="50%" height="50%"/>

<img src="https://github.com/user-attachments/assets/59b31d04-9587-4f2e-9725-40f9122dad3a" alt="drawing" width="50%" height="50%"/>

<img src="https://github.com/user-attachments/assets/76bf133d-0763-4bf3-a030-a82602578377" alt="drawing" width="50%" height="50%"/>

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

# Lab 2 - Electronic Circuits

**[Homepage](./index.html)**

## Task 1 - Calibration

The DC voltage output was calibrated as per the instructions:

| Voltage Setting | Measured Voltage | Error in % FS |
| --------------- | ---------------- | ------------- |
| 3.0 V           | 2.87             | 4.3           |
| 2.5 V           | 2.42             | 3.2           |
| 2.0 V           | 1.95             | 2.5           |
| 1.5 V           | 1.48             | 1.3           |
| 1.0 V           | 1.03             | 3.0           |
| 0.5 V           | 0.56             | 12            |

In order to achieve the correct output voltages for task 2, the following voltage settings for SIG_GEN were calculated.

| Measured Voltage | Voltage Setting |
| ---------------- | --------------- |
| 3.0 V            | 3.13            |
| 2.5 V            | 2.59            |
| 2.0 V            | 2.05            |
| 1.5 V            | 1.52            |
| 1.0 V            | 0.97            |
| 0.5 V            | 0.43            |

## Task 2 - Finding the source resistance of SIG_GEN

| V (measured) | Vs Setting | 10k  | 1k   | 100  | 69   |
| ------------ | ---------- | ---- | ---- | ---- | ---- |
| 3.0          | 3.13       | 3.0  | 2.97 | 2.29 |      |
| 2.0          | 2.05       | 1.9  | 1.97 | 1.92 |      |
| 1.0          | 0.97       | 0.99 | 0.98 | 0.96 |      |

Then, completing the second table for $R_L=69\ \Omega$  only,

| $V_s$ setting | $V_{\text{measured}}$ | $I_{\text{out}}$ | $R_s\ (\Omega)$ |
| ------------- | --------------------- | ---------------- | --------------- |
| 3.0           | 2.87                  | 47.0             |                 |
| 2.0           | 1.95                  | 41.4             |                 |
| 1.0           | 0.97                  | 33.4             |                 |

==n/a==

## Task 3 - Voltage Divider Circuit

- R1 and R2 were set to 10k V each, since current is the same and each resistors has the same value, the voltage at Vout was predicted to be half the (calibrated) SIG_GEN voltage -> 1.44 V. It was measured to be 1.42 V

- By using the ratio of the R1 and R2 resistances, I calculated Vout to be 2.06V. I measured it to be 1.96 V.

- $$
  R_{total}=10k+22k=32k\\
  \implies I=\frac{2.87}{32k}=8.97\times 10^{-5}\\
  \implies V_{R2}=IR_2=8.97\times 10^{-5}\times 22k=1.97 V
  $$

- The same voltages were measured for the AC signal

## Task 4 - Thévenin's Equivalent Network

==n/a==

## Task 5 - Complex Resistor Network (R-2R ladder network)

The ladder network was set up as per the diagram. The 20k resistor was approximated with a 15k, 4.7k and 300 Ohm resistors in series (20 030 Ohms).

When measured, V1 = 0.98 V, V2 = 0.48 V. These line up with my predictions.

==n/a==

## Task 6 - Driving a Light Emitting Diode


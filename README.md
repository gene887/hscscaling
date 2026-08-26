Raw Mark to HSC Mark Polynomial Regression.

The Need:
In the context of the HSC, raw marks are scaled to HSC Marks which determine your band placement (ie Bands 1-6). Since each subject has its own difficulty, scaling varies per subject (e.g. Maths Ext 2 scales better than Maths Standard). Since HSC Trial papers are meant to imitate the actual HSC, you can use your raw mark on the trial to predict what HSC mark you would have recieved if the trial was the actual HSC.
(All the data has been collected from HSC Raw Marks Database: https://rawmarks.info/, a trusted source).

Setup:
1. Install requirements.txt
2. Substitute (Raw Mark / 100)
3. Prediction will be printed on the terminal as well as MAE and R^2 values.

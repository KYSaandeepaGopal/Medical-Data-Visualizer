import unittest
import matplotlib
matplotlib.use('Agg')  # Use a non-interactive backend for tests

from medical_data_visualizer import draw_cat_plot, draw_heat_map

class TestMedicalDataVisualizer(unittest.TestCase):
    def test_draw_cat_plot(self):
        fig = draw_cat_plot()
        self.assertIsNotNone(fig, "draw_cat_plot() should return a matplotlib figure object.")
        self.assertEqual(len(fig.axes), 2, "Cat plot should have 2 subplots (one for each cardio value).")

    def test_draw_heat_map(self):
        fig = draw_heat_map()
        self.assertIsNotNone(fig, "draw_heat_map() should return a matplotlib figure object.")
        self.assertEqual(len(fig.axes), 1, "Heatmap should have 1 subplot.")

if __name__ == '__main__':
    unittest.main()
import unittest
from unittest.mock import patch
from color_utils import (
    closest_color_name,
    rgb_from_color_name,
    optimized_mix_colors,
    validate_rgb_input
)
from exceptions import InvalidRGBValueError, ColorNotFoundError
from color_data import oil_paint_colors

class TestColorUtils(unittest.TestCase):
    def test_closest_color_name(self):
        self.assertEqual(closest_color_name((227, 0, 34)), "Cadmium Red")
        self.assertEqual(closest_color_name((0, 0, 0)), "Ivory Black")
        self.assertEqual(closest_color_name((255, 255, 255)), "Titanium White")

    def test_rgb_from_color_name(self):
        self.assertEqual(rgb_from_color_name("Cadmium Red"), ((227, 0, 34), "Cadmium Red"))
        with self.assertRaises(ColorNotFoundError):
            rgb_from_color_name("NonexistentColor")
        self.assertEqual(rgb_from_color_name("Cadmium Rd"), ((227, 0, 34), "Cadmium Red"))  # Test fuzzy matching

    def test_optimized_mix_colors(self):
        mix = optimized_mix_colors((227, 0, 34), 'medium')  # Cadmium Red
        self.assertIn("Cadmium Red", mix)
        self.assertEqual(sum(mix.values()), 100)

        mix = optimized_mix_colors((0, 255, 0), 'medium')  # Pure Green
        self.assertIn("Cadmium Yellow", mix)
        self.assertIn("Permanent Green", mix)
        self.assertEqual(sum(mix.values()), 100)

    def test_validate_rgb_input(self):
        validate_rgb_input((0, 0, 0))  # Should not raise an exception
        validate_rgb_input((255, 255, 255))  # Should not raise an exception
        
        with self.assertRaises(InvalidRGBValueError):
            validate_rgb_input((256, 0, 0))
        
        with self.assertRaises(InvalidRGBValueError):
            validate_rgb_input((-1, 0, 0))
        
        with self.assertRaises(InvalidRGBValueError):
            validate_rgb_input((0, 0))  # Too few values

    @patch('color_utils.display_color')
    def test_closest_color_name_verbose(self, mock_display_color):
        closest_color = closest_color_name((227, 0, 34), verbose=True)
        self.assertEqual(closest_color, "Cadmium Red")
        mock_display_color.assert_called_once_with((227, 0, 34), "Cadmium Red")

if __name__ == '__main__':
    unittest.main()
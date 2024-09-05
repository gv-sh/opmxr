import argparse
import sys
from typing import Tuple, Dict

from color_data import oil_paint_colors
from color_utils import (
    closest_color_name,
    rgb_from_color_name,
    optimized_mix_colors,
    display_color,
    list_all_colors,
    validate_rgb_input,
    save_to_file,
)
from exceptions import ColorNotFoundError, InvalidRGBValueError

def main():
    parser = argparse.ArgumentParser(description="Oil Paint Color Utility")
    subparsers = parser.add_subparsers(dest="command", help="Available commands")

    closest_color_parser = subparsers.add_parser("closest-color", help="Find closest oil paint color")
    closest_color_parser.add_argument("rgb", nargs=3, type=int, metavar=("R", "G", "B"))

    color_rgb_parser = subparsers.add_parser("color-rgb", help="Find RGB value for given color name")
    color_rgb_parser.add_argument("color_name", type=str)

    mix_color_parser = subparsers.add_parser("mix-color", help="Suggest a mix of basic pigments")
    mix_color_parser.add_argument("rgb", nargs=3, type=int, metavar=("R", "G", "B"))

    mix_name_parser = subparsers.add_parser("mix-name", help="Mix colors to achieve a given color name")
    mix_name_parser.add_argument("color_name", type=str)

    subparsers.add_parser("list-colors", help="List all available oil paint colors")

    for subparser in [mix_color_parser, mix_name_parser]:
        subparser.add_argument("--complexity", choices=['low', 'medium', 'high'], default='medium')

    parser.add_argument("--save", type=str, metavar="FILENAME", help="Save output to a specified file")
    parser.add_argument("--verbose", action='store_true', help="Enable verbose mode for more detailed output")

    args = parser.parse_args()

    try:
        output = ""

        if args.command == "closest-color":
            rgb_value = tuple(args.rgb)
            validate_rgb_input(rgb_value)
            closest_color = closest_color_name(rgb_value, args.verbose)
            output += f"The closest oil paint color is: {closest_color}\n"
            print(output.strip())
            display_color(oil_paint_colors[closest_color], closest_color)
        
        elif args.command == "color-rgb":
            rgb_value, matched_name = rgb_from_color_name(args.color_name)
            if rgb_value:
                output += f"The RGB value for {matched_name} is: {rgb_value}\n"
                print(output.strip())
                display_color(rgb_value, matched_name)
            else:
                raise ColorNotFoundError("Color not found. Please try again.")
        
        elif args.command == "mix-color":
            target_rgb = tuple(args.rgb)
            validate_rgb_input(target_rgb)
            mix_result = optimized_mix_colors(target_rgb, args.complexity)
            output += f"To achieve {target_rgb}, mix the following colors:\n"
            for color, parts in mix_result.items():
                output += f"{color}: {parts} parts\n"
            print(output.strip())
            display_color(target_rgb, "Mixed Color")
        
        elif args.command == "mix-name":
            rgb_value, matched_name = rgb_from_color_name(args.color_name)
            if rgb_value:
                mix_result = optimized_mix_colors(rgb_value, args.complexity)
                output += f"To achieve {matched_name} ({rgb_value}), mix the following colors:\n"
                for color, parts in mix_result.items():
                    output += f"{color}: {parts} parts\n"
                print(output.strip())
                display_color(rgb_value, "Mixed Color")
            else:
                raise ColorNotFoundError("Color not found. Please try again.")
        
        elif args.command == "list-colors":
            list_all_colors()
        
        else:
            parser.print_help()
        
        if args.save and output:
            save_to_file(args.save, output)

    except (ColorNotFoundError, InvalidRGBValueError) as e:
        print(f"Error: {e}")
        sys.exit(1)

if __name__ == "__main__":
    main()
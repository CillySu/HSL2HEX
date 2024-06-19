import colorsys
import sys
import argparse
import re

# Set this to True if you want to print variable names along with hex codes
PRINT_NAMES = True

def hsl_to_hex(h, s, l):
    r, g, b = colorsys.hls_to_rgb(h / 360, l / 100, s / 100)
    return f"#{int(r * 255):02x}{int(g * 255):02x}{int(b * 255):02x}"

def convert_css_hsl_to_hex(css, print_names):
    hsl_pattern = re.compile(r'([\w-]+.* )?hsl\((\d+), (\d+)%, (\d+)%\);')
    
    hex_codes = []
    
    for match in hsl_pattern.finditer(css):
        h = int(match.group(2))
        s = int(match.group(3))
        l = int(match.group(4))
        hex_code = hsl_to_hex(h, s, l)
        
        if print_names:
            hex_codes.append(f"{match.group(1)} {hex_code};")
        else:
            hex_codes.append(hex_code)
    
    return hex_codes

css_hsl_colors = """
    """

def main():
    parser = argparse.ArgumentParser(description="Convert HSL colors in CSS to HEX format.")
    parser.add_argument("file_or_string", help="Path to the CSS file or the CSS string containing HSL colors")
    parser.add_argument("--print-lines", action="store_true", help="Print variable names along with hex codes")
    parser.add_argument("--output", "-o", help="Path to save the output")
    
    args = parser.parse_args()

    # Check if the input is a file path or a string
    if args.file_or_string.endswith('.css'):
        try:
            with open(args.file_or_string, 'r') as file:
                css_hsl_colors = file.read()
        except FileNotFoundError:
            print(f"Error: File '{args.file_or_string}' not found.", file=sys.stderr)
            sys.exit(1)
    else:
        css_hsl_colors = args.file_or_string

    hex_codes = convert_css_hsl_to_hex(css_hsl_colors, args.print_lines)

    output = "\n".join(hex_codes)
    
    if args.output:
        with open(args.output, 'w') as out_file:
            out_file.write(output)
    else:
        print(output)
        
if __name__ == "__main__":
    main()
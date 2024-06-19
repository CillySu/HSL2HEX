import colorsys
import re

def hsl_to_hex(h, s, l):
    r, g, b = colorsys.hls_to_rgb(h/360, 1/100, s/100)
    return f"#{int(r*255):02x}{int(g*255):02x}{int(b*255):02x}"

css_colours = """
:root { 
    --red-0: hsl(0, 69%, 76%);
    --red-1: hsl(0, 71%, 67%);
    --red-2: hsl(0, 73%, 58%);
    --red-3: hsl(0, 76%, 49%);
    --red-4: hsl(0, 79%, 40%);
    --red-5: hsl(0, 83%, 31%);
    --red-6: hsl(0, 87%, 22%);
    --red-7: hsl(0, 92%, 13%);
    --pink-0: hsl(339, 69%, 76%);
    --pink-1: hsl(339, 71%, 67%);
    --pink-2: hsl(339, 73%, 58%);
    --pink-3: hsl(339, 76%, 49%);
    --pink-4: hsl(339, 79%, 40%);
    --pink-5: hsl(339, 83%, 31%);
    --pink-6: hsl(339, 87%, 22%);
    --pink-7: hsl(339, 92%, 13%);
    --grape-0: hsl(288, 69%, 76%);
    --grape-1: hsl(288, 71%, 67%);
    --grape-2: hsl(288, 73%, 58%);
    --grape-3: hsl(288, 76%, 49%);
    --grape-4: hsl(288, 79%, 40%);
    --grape-5: hsl(288, 83%, 31%);
    --grape-6: hsl(288, 87%, 22%);
    --grape-7: hsl(288, 92%, 13%);
    --violet-0: hsl(255, 69%, 76%);
    --violet-1: hsl(255, 71%, 67%);
    --violet-2: hsl(255, 73%, 58%);
    --violet-3: hsl(255, 76%, 49%);
    --violet-4: hsl(255, 79%, 40%);
    --violet-5: hsl(255, 83%, 31%);
    --violet-6: hsl(255, 87%, 22%);
    --violet-7: hsl(255, 92%, 13%);
    --indigo-0: hsl(230, 69%, 76%);
    --indigo-1: hsl(230, 71%, 67%);
    --indigo-2: hsl(230, 73%, 58%);
    --indigo-3: hsl(230, 76%, 49%);
    --indigo-4: hsl(230, 79%, 40%);
    --indigo-5: hsl(230, 83%, 31%);
    --indigo-6: hsl(230, 87%, 22%);
    --indigo-7: hsl(230, 92%, 13%);
    --blue-0: hsl(208, 69%, 76%);
    --blue-1: hsl(208, 71%, 67%);
    --blue-2: hsl(208, 73%, 58%);
    --blue-3: hsl(208, 76%, 49%);
    --blue-4: hsl(208, 79%, 40%);
    --blue-5: hsl(208, 83%, 31%);
    --blue-6: hsl(208, 87%, 22%);
    --blue-7: hsl(208, 92%, 13%);
    --cyan-0: hsl(188, 69%, 76%);
    --cyan-1: hsl(188, 71%, 67%);
    --cyan-2: hsl(188, 73%, 58%);
    --cyan-3: hsl(188, 76%, 49%);
    --cyan-4: hsl(188, 79%, 40%);
    --cyan-5: hsl(188, 83%, 31%);
    --cyan-6: hsl(188, 87%, 22%);
    --cyan-7: hsl(188, 92%, 13%);
    --teal-0: hsl(162, 69%, 76%);
    --teal-1: hsl(162, 71%, 67%);
    --teal-2: hsl(162, 73%, 58%);
    --teal-3: hsl(162, 76%, 49%);
    --teal-4: hsl(162, 79%, 40%);
    --teal-5: hsl(162, 83%, 31%);
    --teal-6: hsl(162, 87%, 22%);
    --teal-7: hsl(162, 92%, 13%);
    --green-0: hsl(131, 69%, 76%);
    --green-1: hsl(131, 71%, 67%);
    --green-2: hsl(131, 73%, 58%);
    --green-3: hsl(131, 76%, 49%);
    --green-4: hsl(131, 79%, 40%);
    --green-5: hsl(131, 83%, 31%);
    --green-6: hsl(131, 87%, 22%);
    --green-7: hsl(131, 92%, 13%);
    --lime-0: hsl(85, 69%, 76%);
    --lime-1: hsl(85, 71%, 67%);
    --lime-2: hsl(85, 73%, 58%);
    --lime-3: hsl(85, 76%, 49%);
    --lime-4: hsl(85, 79%, 40%);
    --lime-5: hsl(85, 83%, 31%);
    --lime-6: hsl(85, 87%, 22%);
    --lime-7: hsl(85, 92%, 13%);
    --yellow-0: hsl(39, 69%, 76%);
    --yellow-1: hsl(39, 71%, 67%);
    --yellow-2: hsl(39, 73%, 58%);
    --yellow-3: hsl(39, 76%, 49%);
    --yellow-4: hsl(39, 79%, 40%);
    --yellow-5: hsl(39, 83%, 31%);
    --yellow-6: hsl(39, 87%, 22%);
    --yellow-7: hsl(39, 92%, 13%);
    --orange-0: hsl(24, 69%, 76%);
    --orange-1: hsl(24, 71%, 67%);
    --orange-2: hsl(24, 73%, 58%);
    --orange-3: hsl(24, 76%, 49%);
    --orange-4: hsl(24, 79%, 40%);
    --orange-5: hsl(24, 83%, 31%);
    --orange-6: hsl(24, 87%, 22%);
    --orange-7: hsl(24, 92%, 13%);
    --grey-0: hsl(0, 0%, 76%);
    --grey-1: hsl(0, 0%, 67%);
    --grey-2: hsl(0, 0%, 58%);
    --grey-3: hsl(0, 0%, 49%);
    --grey-4: hsl(0, 0%, 40%);
    --grey-5: hsl(0, 0%, 31%);
    --grey-6: hsl(0, 0%, 22%);
    --grey-7: hsl(0, 0%, 13%); }
"""

def css_hsl_to_hex(css):
    hsl_pattern = re.compile(r'(hsl\((\d+), (\d+)%, (\d+)%\))')
    def replace_hsl(match):
        h = int(match.group(2))
        s = int(match.group(3))
        l = int(match.group(4))
        return hsl_to_hex(h, s, l)
    return hsl_pattern.sub(lambda m: replace_hsl(m), css)

converted_css = convert_css_hsl_to_hex(css_colours)
print(converted_css)

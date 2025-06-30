class colorPalette:
    """
    A utility class for managing and converting color palettes.

    Features:
    - Uses a default hardcoded color list or loads a color set from Seaborn.
    - Converts hex color codes to RGB or normalized RGB (0 to 1 floats).
    - Allows indexing colors by integer or predefined single-letter shortcuts when using default or 'Set1' palette.

    Attributes:
    -----------
    colorset : str or None
        Name of the seaborn color palette to use. If None, uses a default hardcoded palette.
    colors : list of str
        List of colors in hex format.
    sns : module (optional)
        Seaborn module imported only if a colorset is specified.

    Methods:
    --------
    hex2rgb(hex):
        Converts a hex color string (e.g., '#ff0000') to a list of RGB integers [R, G, B].

    hex2rgb_normalize(hex):
        Converts a hex color string to a list of RGB floats normalized between 0 and 1.

    rgb(color_ind):
        Returns the RGB integer list for a given color index or shortcut character.

    rgb_normalize(color_ind):
        Returns the normalized RGB float list for a given color index or shortcut character.

    Example:
    --------
    cp = colorPalette()
    print(cp.rgb('r'))           # [228, 26, 28]
    print(cp.rgb_normalize(1))   # normalized RGB for the second color
    """
    def __init__(self, colorset=None) -> None:
        self.colorset = colorset
        if colorset is None:
            self.colors = ['#e41a1c', '#377eb8', '#4daf4a', '#984ea3', '#ff7f00', 
                           '#ffff33', '#a65628', '#f781bf', '#999999', '#000000',]
        else:
            import seaborn as sns
            self.sns = sns
            self.colors = self.sns.color_palette(self.colorset).as_hex()
        
    def hex2rgb(self, hex):
        return [int(hex.lstrip('#')[i:i+2], 16) for i in (0, 2, 4)]
    
    def hex2rgb_normalize(self, hex):
        return [int(hex.lstrip('#')[i:i+2], 16)/255.0 for i in (0, 2, 4)]
        
    def rgb(self, color_ind):
        if isinstance(color_ind, str):
            if self.colorset == "Set1" or self.colorset == None:
                color_ind = ['r', 'b', 'g', 'p', 'o', 'y', 'br', 'pi', 'w'].index(color_ind)
        return self.hex2rgb(self.colors[color_ind])
    
    def rgb_normalize(self, color_ind):
        if isinstance(color_ind, str):
            if self.colorset == "Set1" or self.colorset == None:
                color_ind = ['r', 'b', 'g', 'p', 'o', 'y', 'br', 'pi', 'w'].index(color_ind)
        return self.hex2rgb_normalize(self.colors[color_ind])
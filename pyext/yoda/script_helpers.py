import os

def parse_x2y_args(args, xextn, yextn):
    """
    Helper function for working out input and output filenames for YODA
    converter scripts, where the output name is generated by replacing the input
    file extension (xextn) with the output one (yextn), if there are exactly two
    arguments and the second arg is consistent with an output name. The x/yextn
    arguments should include the leading dot.
    """
    infiles = []
    outfiles = []
    ## If there are two args and the second has the right output extension, treat as in-, out-names
    if len(args) == 2 and (args[1].endswith(yextn) or args[1] == "-"):
        infiles = [args[0]]
        outfiles = [args[1]]
    ## Otherwise treat as a list of in-names and generate default out-names
    else:
        for infile in args:
            if infile.endswith(xextn):
                outfile = infile.replace(xextn, yextn)
            else:
                outfile = infile + yextn
            outfile = os.path.basename(outfile)
            infiles.append(infile)
            outfiles.append(outfile)
    return zip(infiles, outfiles)


def filter_aos(aos, match_re=None, unmatch_re=None):
    "Remove unwanted analysis objects from a dict (modifies arg, also returned)"
    import re
    if match_re:
        re_match = re.compile(match_re)
        keylist = list(aos.keys())
        for k in keylist:
            if not re_match.search(k):
                del aos[k]
    if unmatch_re:
        re_unmatch = re.compile(unmatch_re)
        keylist = list(aos.keys())
        for k in keylist:
            if re_unmatch.search(k):
                del aos[k]
    return aos

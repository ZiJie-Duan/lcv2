
def tool_strat(sys):
    if sys == "windows":
        import tool_win
        tool_win.root_tool()
    else:
        import tool_mac
        tool_mac.root_tool()
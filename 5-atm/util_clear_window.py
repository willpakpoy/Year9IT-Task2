def clear_window():
    for widget in window.winfo_children():
        widget.destroy()
"""
    msg = "Anytime you get one of these messages, rest assured you are going to learn something important!"
    MBOX.showinfo( "Take Note!", msg )
    MBOX.showwarning( "Take Note!", msg )
    MBOX.showerror( "Take Note!", msg )
    response = MBOX.askyesno( "Take Note!", msg ) # 1/null?
    response = MBOX.askokcancel( "Take Note!", response ) # 1/null?
    MBOX.showinfo( "Take Note!", response )
""" 
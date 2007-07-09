#!/usr/bin/env ruby

require 'fox16'
require 'fox16/colors'
require 'tabBook'
require 'sand'

include Fox

TYGER = <<END_OF_POEM
Family Tree
END_OF_POEM


class MDITestWindow  < FXMainWindow

  def initialize(app)
    # Invoke base class initialize method first
    super(app, "Legado", :opts => DECOR_ALL, :width => 800, :height => 600)

    # Create the font
    @font = FXFont.new(getApp(), "courier", 15, FONTWEIGHT_BOLD)
    
     # Make some icons
    fileopenicon = getIcon("goslogo.jpg")
    filesaveicon = getIcon("goslogo.jpg")
    cuticon = getIcon("goslogo.jpg")
    copyicon = getIcon("goslogo.jpg")
    pasteicon = getIcon("goslogo.jpg")
    uplevelicon = getIcon("goslogo.jpg")
    paletteicon = getIcon("goslogo.jpg")
    
    


    # Make color dialog
    colordlg = FXColorDialog.new(self, "Color Dialog")
  
    # Menubar
    menubar = FXMenuBar.new(self, LAYOUT_SIDE_TOP|LAYOUT_FILL_X)
    
  
    # Status bar
    FXStatusBar.new(self,
      LAYOUT_SIDE_BOTTOM|LAYOUT_FILL_X|STATUSBAR_WITH_DRAGCORNER)
      
    # Docking sites
    topDockSite = FXDockSite.new(self, LAYOUT_SIDE_TOP|LAYOUT_FILL_X)
    FXDockSite.new(self, LAYOUT_SIDE_BOTTOM|LAYOUT_FILL_X)
    FXDockSite.new(self, LAYOUT_SIDE_LEFT|LAYOUT_FILL_Y)
    FXDockSite.new(self, LAYOUT_SIDE_RIGHT|LAYOUT_FILL_Y)
 
     
    # Tool bar is docked inside the top one for starters
    toolbarShell = FXToolBarShell.new(self)
    toolbar = FXToolBar.new(topDockSite, toolbarShell,
    PACK_UNIFORM_WIDTH|PACK_UNIFORM_HEIGHT|FRAME_RAISED|LAYOUT_FILL_X)
    FXToolBarGrip.new(toolbar, toolbar, FXToolBar::ID_TOOLBARGRIP, TOOLBARGRIP_DOUBLE)

  
     # Toobar buttons: Editing
    FXButton.new(toolbar, "Cut\tCut", cuticon,
      :opts => ICON_ABOVE_TEXT|BUTTON_TOOLBAR|FRAME_RAISED)
    FXButton.new(toolbar, "Copy\tCopy", copyicon,
      :opts => ICON_ABOVE_TEXT|BUTTON_TOOLBAR|FRAME_RAISED)
    FXButton.new(toolbar, "Paste\tPaste", pasteicon,
      :opts => ICON_ABOVE_TEXT|BUTTON_TOOLBAR|FRAME_RAISED)
  
    # Color
    FXButton.new(toolbar, "&Colors\tColors\tDisplay color dialog.", paletteicon,
      colordlg, FXWindow::ID_SHOW,
      ICON_ABOVE_TEXT|BUTTON_TOOLBAR|FRAME_RAISED|LAYOUT_RIGHT)
      
      
    # MDI Client
    @mdiclient = FXMDIClient.new(self, LAYOUT_FILL_X|LAYOUT_FILL_Y)
  
    # Icon for MDI Child
    @mdiicon = nil
    File.open(File.join("icons", "goslogo.jpg"), "rb") do |f|
      @mdiicon = FXPNGIcon.new(getApp(), f.read)
    end

    # Make MDI Menu
    @mdimenu = FXMDIMenu.new(self, @mdiclient)
  
    # MDI buttons in menu:- note the message ID's!!!!!
    # Normally, MDI commands are simply sensitized or desensitized;
    # Under the menubar, however, they're hidden if the MDI Client is
    # not maximized.  To do this, they must have different ID's.
    FXMDIWindowButton.new(menubar, @mdimenu, @mdiclient, FXMDIClient::ID_MDI_MENUWINDOW,
      LAYOUT_LEFT)
    FXMDIDeleteButton.new(menubar, @mdiclient, FXMDIClient::ID_MDI_MENUCLOSE,
      FRAME_RAISED|LAYOUT_RIGHT)
    FXMDIRestoreButton.new(menubar, @mdiclient, FXMDIClient::ID_MDI_MENURESTORE,
      FRAME_RAISED|LAYOUT_RIGHT)
    FXMDIMinimizeButton.new(menubar, @mdiclient,
      FXMDIClient::ID_MDI_MENUMINIMIZE, FRAME_RAISED|LAYOUT_RIGHT)
  
    # Create a few test windows to get started
    mdichild = createTestWindow(10, 10, 400, 300)
    @mdiclient.setActiveChild(mdichild)
    createTestWindow(20, 20, 400, 300)
    createTestWindow(30, 30, 400, 300)
  
    # File menu
    filemenu = FXMenuPane.new(self)
    newCmd = FXMenuCommand.new(filemenu, "&New\tCtl-N\tCreate new document.")
    newCmd.connect(SEL_COMMAND, method(:onCmdNew))
    FXMenuCommand.new(filemenu, "&Quit\tCtl-Q\tQuit application.", nil,
      getApp(), FXApp::ID_QUIT, 0)
    FXMenuTitle.new(menubar, "&File", nil, filemenu)
      
    # Window menu
    windowmenu = FXMenuPane.new(self)
    FXMenuCommand.new(windowmenu, "Tile &Horizontally", nil,
      @mdiclient, FXMDIClient::ID_MDI_TILEHORIZONTAL)
    FXMenuCommand.new(windowmenu, "Tile &Vertically", nil,
      @mdiclient, FXMDIClient::ID_MDI_TILEVERTICAL)
    FXMenuCommand.new(windowmenu, "C&ascade", nil,
      @mdiclient, FXMDIClient::ID_MDI_CASCADE)
    FXMenuCommand.new(windowmenu, "&Close", nil,
      @mdiclient, FXMDIClient::ID_MDI_CLOSE)
    sep1 = FXMenuSeparator.new(windowmenu)
    sep1.setTarget(@mdiclient)
    sep1.setSelector(FXMDIClient::ID_MDI_ANY)
    FXMenuCommand.new(windowmenu, nil, nil, @mdiclient, FXMDIClient::ID_MDI_1)
    FXMenuCommand.new(windowmenu, nil, nil, @mdiclient, FXMDIClient::ID_MDI_2)
    FXMenuCommand.new(windowmenu, nil, nil, @mdiclient, FXMDIClient::ID_MDI_3)
    FXMenuCommand.new(windowmenu, nil, nil, @mdiclient, FXMDIClient::ID_MDI_4)
    FXMenuCommand.new(windowmenu, "&Others...", nil, @mdiclient, FXMDIClient::ID_MDI_OVER_5)
    FXMenuTitle.new(menubar,"&Window", nil, windowmenu)
    
    # Help menu
    helpmenu = FXMenuPane.new(self)
    FXMenuCommand.new(helpmenu, "&About FOX...").connect(SEL_COMMAND) {
      FXMessageBox.information(self, MBOX_OK, "About MDI Test",
        "Test of the FOX MDI Widgets\nWritten by Jeroen van der Zijp")
    }
    FXMenuTitle.new(menubar, "&Help", nil, helpmenu, LAYOUT_RIGHT)
  end

  # Create a new MDI child window
  def createTestWindow(x, y, w, h)
   
    mdichild = FXMDIChild.new(@mdiclient, "Child", @mdiicon, @mdimenu,0, x, y, w, h)
    scrollwindow = FXScrollWindow.new(mdichild, 0)
    scrollwindow.verticalScrollBar.setLine(@font.fontHeight)
    btn = FXButton.new(scrollwindow, TYGER,:opts => LAYOUT_FIX_WIDTH|LAYOUT_FIX_HEIGHT, :width => 50, :height => 50)
    btn.font = @font
    btn.backColor = FXColor::White

    # Menubar appears along the top of the main window
    menubar = FXMenuBar.new(self, LAYOUT_SIDE_TOP|LAYOUT_FILL_X)
    
      # Separator
    FXHorizontalSeparator.new(self,
      LAYOUT_SIDE_TOP|LAYOUT_FILL_X|SEPARATOR_GROOVE)

    # Contents
    contents = FXHorizontalFrame.new(self,
      LAYOUT_SIDE_TOP|FRAME_NONE|LAYOUT_FILL_X|LAYOUT_FILL_Y|PACK_UNIFORM_WIDTH)

 # Switcher
    @tabbook = FXTabBook.new(contents,:opts => LAYOUT_FILL_X|LAYOUT_FILL_Y|LAYOUT_RIGHT)
  
    # First item is a list
    @tab1 = FXTabItem.new(@tabbook, "&Simple List", nil)
    listframe = FXHorizontalFrame.new(@tabbook, FRAME_THICK|FRAME_RAISED)
    simplelist = FXList.new(listframe, :opts => LIST_EXTENDEDSELECT|LAYOUT_FILL_X|LAYOUT_FILL_Y)
    simplelist.appendItem("First Entry")
    simplelist.appendItem("Second Entry")
    simplelist.appendItem("Third Entry")
    simplelist.appendItem("Fourth Entry")

    
#    TabBookWindow.new(mdichild);
    #     # Contents
#    frame = FXHorizontalFrame.new(mdichild,
#    LAYOUT_SIDE_TOP|LAYOUT_FILL_X|LAYOUT_FILL_Y, :padding => 0, :hSpacing => 0, :vSpacing => 0)
##
##     # Tab book with switchable panels
#    panels = TabBook.new(frame, mdichild)

    mdichild
  end
  
  # Convenience function to construct a PNG icon
  def getIcon(filename)
    begin
      filename = File.join("icons", filename)
      icon = nil
      File.open(filename, "rb") do |f|
        icon = FXPNGIcon.new(getApp(), f.read)
      end
      icon
    rescue
      raise RuntimeError, "Couldn't load icon: #{filename}"
    end
  end

  # New
  def onCmdNew(sender, sel, ptr)
    mdichild = createTestWindow(20, 20, 300, 200)
    mdichild.create
    return 1
  end

  # Start
  def create
    super

    # At the time the first three MDI windows are constructed, we don't
    # yet know the font height and so we cannot accurately set the line
    # height for the vertical scrollbar. Now that the real font has been
    # created, we can go back and fix the scrollbar line heights for these
    # windows.
    @font.create
    @mdiclient.each_child do |mdichild|
      mdichild.contentWindow.verticalScrollBar.setLine(@font.fontHeight)
    end

    show(PLACEMENT_SCREEN)
  end
end

if __FILE__ == $0
  # Make application
  application = FXApp.new("MDI LEGADO", "FoxTest")
  
  # Make window
  MDITestWindow.new(application)
  
  # Create app
  application.create
  
  # Run
  application.run
end

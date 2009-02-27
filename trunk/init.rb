#!/usr/bin/env ruby

require 'fox16'
require 'fox16/colors'
require 'util'
require 'apifunc'
require 'roxml'
require 'model'
include Fox


class MDITestWindow  < FXMainWindow
include Util
include ApiFunc

  def initialize(app)
  @username = "api-user-1033" # 
  @password = "104c" # 
  $childrenIds=nil
  $simplelist=nil
  $id = ''
  titleFont = nil
  $results=nil
  titleFont = FXFont.new(app, "Arial",11,700)
  
  super(app, "Legado", :opts => DECOR_ALL, :width => 800, :height => 600)
   setupLayout(app)
    
   loginApi(@username, @password)
####################################

    
#    # Menubar appears along the top of the main window
#    menubar = FXMenuBar.new(self, LAYOUT_SIDE_TOP|LAYOUT_FILL_X)

  # Separator
    FXHorizontalSeparator.new(self,
      LAYOUT_SIDE_TOP|LAYOUT_FILL_X|SEPARATOR_GROOVE)

  # Contents
    contents = FXHorizontalFrame.new(self,
      LAYOUT_SIDE_TOP|FRAME_NONE|LAYOUT_FILL_X|LAYOUT_FILL_Y|PACK_UNIFORM_WIDTH)

     # Switcher
    @tabbook = FXTabBook.new(contents,:opts => LAYOUT_FILL_X|LAYOUT_FILL_Y|LAYOUT_RIGHT)
  
    # First item is a list
     $id ='p.14000009244'
      treeid =  getTreeId($id)
      treeinfo = getTreeInfo(treeid)
    
    @rootname = FXDataTarget.new(treeinfo[0])
    @momname = FXDataTarget.new(treeinfo[1])
    @dadname = FXDataTarget.new(treeinfo[2])
    @grandma1 = FXDataTarget.new(treeinfo[5])
    @grandpa1 = FXDataTarget.new(treeinfo[6])
    @grandma2 = FXDataTarget.new(treeinfo[3])
    @grandpa2 = FXDataTarget.new(treeinfo[4])
    
    displaysize = 30
    @tab1 = FXTabItem.new(@tabbook, "&Pedigree", nil)
    tab2contents = FXHorizontalFrame.new(@tabbook,LAYOUT_FILL_X|LAYOUT_FILL_Y|FRAME_THICK|FRAME_RAISED)
    rootframe = FXVerticalFrame.new(tab2contents,LAYOUT_FILL_X|LAYOUT_FILL_Y|FRAME_THICK|LAYOUT_CENTER_Y)
    ancestorframe= FXVerticalFrame.new(tab2contents,LAYOUT_FILL_X|LAYOUT_FILL_Y|FRAME_THICK)
    dadframe = FXHorizontalFrame.new(ancestorframe,LAYOUT_FILL_X|LAYOUT_FILL_Y|FRAME_THICK)
    momframe = FXHorizontalFrame.new(ancestorframe,LAYOUT_FILL_X|LAYOUT_FILL_Y|FRAME_THICK)
    rootinput = FXTextField.new(rootframe, displaysize, @rootname, FXDataTarget::ID_VALUE,LAYOUT_CENTER_Y)
    
    FXTextField.new(dadframe, displaysize, @dadname, FXDataTarget::ID_VALUE,LAYOUT_CENTER_Y)
    FXTextField.new(momframe, displaysize, @momname, FXDataTarget::ID_VALUE,LAYOUT_CENTER_Y)
    grandparentsframe= FXVerticalFrame.new(tab2contents,LAYOUT_FILL_X|LAYOUT_FILL_Y|FRAME_THICK)
    grandpa1frame = FXHorizontalFrame.new(grandparentsframe,LAYOUT_FILL_X|LAYOUT_FILL_Y|FRAME_THICK)
    grandma1frame = FXHorizontalFrame.new(grandparentsframe,LAYOUT_FILL_X|LAYOUT_FILL_Y|FRAME_THICK)
    grandpa2frame = FXHorizontalFrame.new(grandparentsframe,LAYOUT_FILL_X|LAYOUT_FILL_Y|FRAME_THICK)
    grandma2frame = FXHorizontalFrame.new(grandparentsframe,LAYOUT_FILL_X|LAYOUT_FILL_Y|FRAME_THICK)
    FXTextField.new(grandpa1frame, displaysize, @grandpa1, FXDataTarget::ID_VALUE,LAYOUT_CENTER_Y)
    FXTextField.new(grandma1frame, displaysize, @grandma1, FXDataTarget::ID_VALUE,LAYOUT_CENTER_Y)
    FXTextField.new(grandpa2frame, displaysize, @grandpa2, FXDataTarget::ID_VALUE,LAYOUT_CENTER_Y)
    FXTextField.new(grandma2frame, displaysize, @grandma2, FXDataTarget::ID_VALUE,LAYOUT_CENTER_Y)
    
  
        ############## Family Tab
    spouseId = getSpouses($id)[0] 
    dadId = getParents($id)[1]
    momId = getParents($id)[0]
    $childrenIds = getChildren($id)
    
    
    @metxt =FXDataTarget.new(getInfo($id))
    @spousetxt=FXDataTarget.new(getInfo(spouseId))
    @dadtxt = FXDataTarget.new(getInfo(dadId))
    @momtxt = FXDataTarget.new(getInfo(momId))
    
    @familytab = FXTabItem.new(@tabbook, "&Family", nil)
    famtabcontents = FXHorizontalFrame.new(@tabbook,LAYOUT_FILL_X|LAYOUT_FILL_Y|FRAME_THICK|FRAME_RAISED)
    ancestorframe= FXVerticalFrame.new(famtabcontents,LAYOUT_FILL_X|LAYOUT_FILL_Y|FRAME_THICK)
    dadframe = FXHorizontalFrame.new(ancestorframe,LAYOUT_FILL_X|LAYOUT_FILL_Y|FRAME_THICK)
    momframe = FXHorizontalFrame.new(ancestorframe,LAYOUT_FILL_X|LAYOUT_FILL_Y|FRAME_THICK)
    dadLabel = FXLabel.new(dadframe, "Dad", nil)
    dadLabel.setFont(titleFont)
    @dadbutton = FXButton.new(dadframe, @dadtxt.value, nil,nil,0,FRAME_THICK|LAYOUT_CENTER_Y|ICON_BEFORE_TEXT)
    @dadbutton.connect(SEL_COMMAND)do
    $id =getParents($id)[1]
    updateTab($id)
  end
  momLabel = FXLabel.new(momframe, "Mom", nil)
  momLabel.setFont(titleFont)
  @mombutton = FXButton.new(momframe, @momtxt.value, nil,nil,0,FRAME_THICK|LAYOUT_CENTER_Y|ICON_BEFORE_TEXT)
  @mombutton.connect(SEL_COMMAND)do
  $id =getParents($id)[0]
  updateTab($id)
end

rootframe = FXVerticalFrame.new(famtabcontents,LAYOUT_FILL_X|LAYOUT_FILL_Y|FRAME_THICK|LAYOUT_CENTER_Y)
meframe = FXHorizontalFrame.new(rootframe,LAYOUT_FILL_X|LAYOUT_FILL_Y|FRAME_THICK)
spouseframe = FXHorizontalFrame.new(rootframe,LAYOUT_FILL_X|LAYOUT_FILL_Y|FRAME_THICK)
meLabel = FXLabel.new(meframe, "Me", nil)
meLabel.setFont(titleFont)
@rootinput = FXTextField.new(meframe, displaysize, @metxt, FXDataTarget::ID_VALUE,LAYOUT_CENTER_Y)
spouseLabel = FXLabel.new(spouseframe, "Spouse", nil)
spouseLabel.setFont(titleFont)
@spousebutton = FXButton.new(spouseframe,@spousetxt.value , nil,@spousetxt,0,FRAME_THICK|LAYOUT_CENTER_Y|ICON_BEFORE_TEXT)
@spousebutton.connect(SEL_COMMAND)do
$id =getSpouses($id)[0]
updateTab($id)
end

childrenframe= FXVerticalFrame.new(famtabcontents,LAYOUT_FILL_X|LAYOUT_FILL_Y|FRAME_THICK)
childrenLabel = FXLabel.new(childrenframe, "Children", nil)
childrenLabel.setFont(titleFont)
@childrenlist = FXList.new(childrenframe, :opts => LIST_EXTENDEDSELECT|LAYOUT_FILL_X|LAYOUT_FILL_Y)
$childrenIds.each{|child|
@childrenlist.appendItem(getInfo(child))
}
###############



################ Search Tab

# Create a data target with an integer value
@intTarget = FXDataTarget.new("joseph+smith")

# First item is a list
@tab2 = FXTabItem.new(@tabbook, "&Search", nil)

# Arrange nicely
tab1contents = FXHorizontalFrame.new(@tabbook,LAYOUT_FILL_X|LAYOUT_FILL_Y|FRAME_THICK|FRAME_RAISED)

# First row
FXLabel.new(tab1contents, "&Root", nil)
input= FXTextField.new(tab1contents, 15, @intTarget, FXDataTarget::ID_VALUE)
# Accept
$results =nil
searchBtn = FXButton.new(tab1contents, "&Search", nil, app, FXDialogBox::ID_ACCEPT,FRAME_RAISED|FRAME_THICK)

# XML output
bottomFrame = FXVerticalFrame.new(tab1contents, LAYOUT_FILL_X|LAYOUT_FILL_Y)

contents = FXVerticalFrame.new(bottomFrame,
                               FRAME_SUNKEN|FRAME_THICK|LAYOUT_SIDE_TOP|LAYOUT_FILL_X|LAYOUT_FILL_Y,
                               :padLeft => 0, :padRight => 0, :padTop => 0, :padBottom => 0,
                               :hSpacing => 0, :vSpacing => 0)

# Make header control
@header1 = FXHeader.new(contents, 
                        :opts => HEADER_BUTTON|HEADER_RESIZE|FRAME_RAISED|FRAME_THICK|LAYOUT_FILL_X)
@header1.connect(SEL_CHANGED) do |sender, sel, which|
@lists[which].width = @header1.getItemSize(which)
end
@header1.connect(SEL_COMMAND) do |sender, sel, which|
@lists[which].numItems.times do |i|
  @lists[which].selectItem(i)
end
end 

FXLabel.new(bottomFrame, "Parsed Result", nil, LAYOUT_FILL_X)
@header1.appendItem("Name", nil, 150)
#    @header1.appendItem("Type", nil, 140)

# Below header
panes = FXHorizontalFrame.new(contents,
                              FRAME_SUNKEN|FRAME_THICK|LAYOUT_SIDE_TOP|LAYOUT_FILL_X|LAYOUT_FILL_Y,
                              :padLeft => 0, :padRight => 0, :padTop => 0, :padBottom => 0,
                              :hSpacing => 0, :vSpacing => 0)

# Make 4 lists
@lists = []
@lists.push(FXList.new(panes, :opts => LAYOUT_FILL_Y|LAYOUT_FIX_WIDTH|LIST_BROWSESELECT,   :width => 200))
#    @lists.push(FXList.new(panes, :opts => LAYOUT_FILL_Y|LAYOUT_FIX_WIDTH|LIST_SINGLESELECT,   :width => 140))

@lists[0].backColor = FXRGB(255, 255, 255)
#    @lists[1].backColor = FXRGB(240, 255, 240)

# Add some contents

searchBtn.connect(SEL_COMMAND) do
@lists[0].clearItems()
$results = getSearchResults(input.text)
$results.each{|result|
  @lists[0].appendItem(result['name']+"     "+ result['score'])
}
#       $results.each{|result|
#       @lists[1].appendItem(result)
#     }

#  @xmlText.txt = 
end

@lists[0].connect(SEL_DOUBLECLICKED,method(:onNameClicked))
# Whip out a tooltip control, jeez, that's hard
FXToolTip.new(getApp())


#   @parsedText = FXText.new(bottomFrame, :opts => TEXT_WORDWRAP |LAYOUT_FILL_X|LAYOUT_FILL_Y|200|200)
#FXLabel.new(bottomFrame, "XML Result:", nil, LAYOUT_FILL_X)
#@xmlText = FXText.new(bottomFrame, :opts => TEXT_WORDWRAP |LAYOUT_FILL_X|LAYOUT_FILL_Y|200|200)    

    
    
    ###############Info Tab########################
    
    @edittab = FXTabItem.new(@tabbook, "&Edit", nil)
    @tabbook.connect(SEL_COMMAND,method(:onSelectedTab))
    edittabcontents = FXHorizontalFrame.new(@tabbook,LAYOUT_FILL_X|LAYOUT_FILL_Y|FRAME_THICK|FRAME_RAISED)
    infoFrame = FXVerticalFrame.new(edittabcontents, LAYOUT_FILL_X|LAYOUT_FILL_Y|LAYOUT_RIGHT|FRAME_SUNKEN|FRAME_THICK)

    infohash = getInfo2($id)
    @name = FXDataTarget.new(infohash['name'])
    @gender = FXDataTarget.new(infohash['gender'])
    @birthdate = FXDataTarget.new(infohash['birthdate'])
    @birthplace = FXDataTarget.new(infohash['birthplace'])
    @deathdate= FXDataTarget.new(infohash['deathdate'])
    @deathplace = FXDataTarget.new(infohash['deathplace'])


    infoBox = FXGroupBox.new(infoFrame, "Info", GROUPBOX_NORMAL|LAYOUT_FILL_X|FRAME_GROOVE)
    infoMatrix = FXMatrix.new(infoBox, 2, MATRIX_BY_COLUMNS|LAYOUT_FILL_X|LAYOUT_FILL_Y)
    FXLabel.new(infoMatrix, "Name:")
    FXTextField.new(infoMatrix, 20, @name, FXDataTarget::ID_VALUE, TEXTFIELD_NORMAL|LAYOUT_FILL_X|LAYOUT_FILL_COLUMN)
    FXLabel.new(infoMatrix, "Gender")
    FXTextField.new(infoMatrix, 20, @gender, FXDataTarget::ID_VALUE, TEXTFIELD_NORMAL|LAYOUT_FILL_X|LAYOUT_FILL_COLUMN)
    FXLabel.new(infoMatrix, "Birthdate")
    FXTextField.new(infoMatrix, 20, @birthdate, FXDataTarget::ID_VALUE, TEXTFIELD_NORMAL|LAYOUT_FILL_X|LAYOUT_FILL_COLUMN)
    FXLabel.new(infoMatrix, "Birth Place")
    FXTextField.new(infoMatrix, 20, @birthplace, FXDataTarget::ID_VALUE, TEXTFIELD_NORMAL|LAYOUT_FILL_X|LAYOUT_FILL_COLUMN)
    FXLabel.new(infoMatrix, "Death Date")
    FXTextField.new(infoMatrix, 20, @deathdate, FXDataTarget::ID_VALUE, TEXTFIELD_NORMAL|LAYOUT_FILL_X|LAYOUT_FILL_COLUMN)
    FXLabel.new(infoMatrix, "Death Place")
    FXTextField.new(infoMatrix, 20, @deathplace, FXDataTarget::ID_VALUE, TEXTFIELD_NORMAL|LAYOUT_FILL_X|LAYOUT_FILL_COLUMN)
    committbtn = FXButton.new(infoMatrix, "&Commit", nil, app, FXDialogBox::ID_ACCEPT,FRAME_RAISED|FRAME_THICK|LAYOUT_FILL_X|LAYOUT_FILL_COLUMN)
    committbtn.connect(SEL_COMMAND) do
      xml= File.read("update.xml")
      xml.sub!("nametoken",@name.value)
      xml.sub!("birthdatetoken",@birthdate.value)
      xml.sub!("birthplacetoken",@birthplace.value)
      xml.sub!("deathdatetoken",@deathdate.value)
      xml.sub!("deathplacetoken",@deathplace.value)
  #    print xml
      uri = "/familytree/v1/person/"+$id
      print postApi(uri, xml)
      FXMessageBox.information(self,MBOX_OK,"Yay! I love NFS","Changes Committed")
    end
    
  
    
    
#    # File Menu
#    filemenu = FXMenuPane.new(self)
#    FXMenuCommand.new(filemenu, "&Simple List", nil,
#      @tabbook, FXTabBar::ID_OPEN_FIRST+0)
#    FXMenuCommand.new(filemenu, "F&ile List", nil,
#      @tabbook, FXTabBar::ID_OPEN_FIRST+1)
#    FXMenuCommand.new(filemenu, "T&ree List", nil,
#      @tabbook, FXTabBar::ID_OPEN_FIRST+2)
#    FXMenuCommand.new(filemenu, "&Quit\tCtl-Q", nil,
#      getApp(), FXApp::ID_QUIT)
#    FXMenuTitle.new(menubar, "&File", nil, filemenu)
#    tabmenu = FXMenuPane.new(self)
#    FXMenuSeparator.new(tabmenu)
#    FXMenuTitle.new(menubar, "&Tab Placement", nil, tabmenu)

    
  end
  def onNameClicked(sender,sel,data)
print data
$id = $results[data]['id']
print "id: "+$id
@tabbook.setCurrent(1)
updateFamilyTab($id)

end
def updateFamilyTab(id)
famhash = getFamInfo(id)
@metxt.value =getInfo(famhash['me'])
@spousebutton.text=getInfo(famhash['spouses'][0])
@dadbutton.text = getInfo(famhash['dad'])
@mombutton.text = getInfo(famhash['mom'])
if @childrenlist.getNumItems >0
@childrenlist.clearItems()
end

famhash['children'].each{|child|
@childrenlist.appendItem(getInfo(child))
@childrenlist.connect(SEL_DOUBLECLICKED,method(:onChildrenClicked))
}
end
def onChildrenClicked(sender,sel,data)
print data
$id = $childrenIds[data]
sender.clearItems()
updateTab($id)

end
  
   def onSelectedTab(sender,sel,data)
   
    print data
    case data
      when 3: updateEditTab($id)
      else
    end
#    FXMessageBox.information(self, MBOX_OK, sender+sel+data, "FXRuby Sample Application")
  end
  def updateEditTab(id)
    infohash = getInfo2(id)
    @name.value = infohash['name']
    @gender.value = infohash['gender']
    @birthdate.value = infohash['birthdate']
    @birthplace.value = infohash['birthplace']
    @deathdate.value= infohash['deathdate']
    @deathplace.value = infohash['deathplace']
  end
  def onChildrenClicked(sender,sel,data)
    print data
   id = $childrenIds[data]
   sender.clearItems()
   updateTab(id)
    
  end
   def updateTab(id)
   print id
    spouseId = getSpouses(id)[0] 
    dadId = getParents(id)[1]
    momId = getParents(id)[0]
    $childrenIds = getChildren(id)
  
    @metxt.value=getInfo(id)
    @spousebutton.text = getInfo(getSpouses(id)[0])
    @dadbutton.text =getInfo(dadId)
    @mombutton.text =getInfo(momId)
   
     @childrenlist.clearItems()
    
    $childrenIds.each{|child|
    @childrenlist.appendItem(getInfo(child))
    @childrenlist.connect(SEL_DOUBLECLICKED,method(:onChildrenClicked))
    }
    
  end
end

class FXTestDialog < FXDialogBox

  def initialize(owner)
    # Invoke base class initialize function first
    super(owner, "Test of Dialog Box", DECOR_TITLE|DECOR_BORDER)

    # Bottom buttons
    buttons = FXHorizontalFrame.new(self,
      LAYOUT_SIDE_BOTTOM|FRAME_NONE|LAYOUT_FILL_X|PACK_UNIFORM_WIDTH,
      :padLeft => 40, :padRight => 40, :padTop => 20, :padBottom => 20)

    # Separator
    FXHorizontalSeparator.new(self,
      LAYOUT_SIDE_BOTTOM|LAYOUT_FILL_X|SEPARATOR_GROOVE)
  
    # Contents
    contents = FXHorizontalFrame.new(self,
      LAYOUT_SIDE_TOP|FRAME_NONE|LAYOUT_FILL_X|LAYOUT_FILL_Y|PACK_UNIFORM_WIDTH)
  
    submenu = FXMenuPane.new(self)
    FXMenuCommand.new(submenu, "One")
    FXMenuCommand.new(submenu, "Two")
    FXMenuCommand.new(submenu, "Three")
    
    # Menu
    menu = FXMenuPane.new(self)
    FXMenuCommand.new(menu, "&Accept", nil, self, ID_ACCEPT)
    FXMenuCommand.new(menu, "&Cancel", nil, self, ID_CANCEL)
    FXMenuCascade.new(menu, "Submenu", nil, submenu)
    FXMenuCommand.new(menu, "&Quit\tCtl-Q", nil, getApp(), FXApp::ID_QUIT)
  
    # Popup menu
    pane = FXPopup.new(self)
    %w{One Two Three Four Five Six Seven Eight Nine Ten}.each do |s|
      FXOption.new(pane, s, :opts => JUSTIFY_HZ_APART|ICON_AFTER_TEXT)
    end
  
    # Option menu
    FXOptionMenu.new(contents, pane, (FRAME_RAISED|FRAME_THICK|
      JUSTIFY_HZ_APART|ICON_AFTER_TEXT|LAYOUT_CENTER_X|LAYOUT_CENTER_Y))

    # Button to pop menu
    FXMenuButton.new(contents, "&Menu", nil, menu, (MENUBUTTON_DOWN|
      JUSTIFY_LEFT|LAYOUT_TOP|FRAME_RAISED|FRAME_THICK|ICON_AFTER_TEXT|
      LAYOUT_CENTER_X|LAYOUT_CENTER_Y))

    # Accept
    accept = FXButton.new(buttons, "&Accept", nil, self, ID_ACCEPT,
      FRAME_RAISED|FRAME_THICK|LAYOUT_RIGHT|LAYOUT_CENTER_Y)
  
    # Cancel
    FXButton.new(buttons, "&Cancel", nil, self, ID_CANCEL,
      FRAME_RAISED|FRAME_THICK|LAYOUT_RIGHT|LAYOUT_CENTER_Y)
    
    accept.setDefault  
    accept.setFocus
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



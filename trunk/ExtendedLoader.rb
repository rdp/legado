require "Loader"
class Loader
    #events
    def init

        runButton.connect(Fox::SEL_COMMAND){
            
						resultTextArea.text='filename.text'
            puts filename.text
				}

    end   # of events
end

#unit test
if __FILE__==$0
	require 'libGUIb16'
	app=FX::App.new
	w=Loader.new app
	w.topwin.show(Fox::PLACEMENT_SCREEN)
	app.create
	app.run
end

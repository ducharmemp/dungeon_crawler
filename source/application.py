"""Copyright (c) 2016 Matthew DuCharme

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated 
documentation files (the "Software"), to deal in the Software without restriction, including without limitation the 
rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit 
persons to whom the Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions 
of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE 
WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS 
OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, 
TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
"""

import atexit

import sdl2
import sdl2.ext

from source.input import InputManager, InputComponent

RESOURCES = sdl2.ext.Resources(__file__, "../resources")


class DummyEntity(sdl2.ext.Entity):
    def __init__(self, world):
        super(DummyEntity, self).__init__()
        self.inputcomponent = InputComponent()


class Application(object):
    def __init__(self):
        sdl2.ext.init()
        self.window = sdl2.ext.Window("Hello World!", size=(640, 480))
        self.running = True
        self.world = sdl2.ext.World()
        self.world.add_system(InputManager())
        self.sprite_factory = sdl2.ext.SpriteFactory(sdl2.ext.SOFTWARE)
        self.dummy = DummyEntity(self.world)

    def run(self):
        self.window.show()
        while self.running:
            events = sdl2.ext.get_events()
            for event in events:
                if event.type == sdl2.SDL_QUIT:
                    self.running = False
                    break
            self.world.process()


if __name__ == '__main__':
    Application().run()
    atexit.register(sdl2.ext.quit)
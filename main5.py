from jnius import autoclass
autoclass('android.content.Intent').out.println('Hello world')

from kivy.setupconfig import USE_SDL2


def share(path):
    if platform == 'android':
        from jnius import cast
        from jnius import autoclass
        if USE_SDL2:
            PythonActivity = autoclass('org.kivy.android.PythonActivity')
        else:
            PythonActivity = autoclass('org.renpy.android.PythonActivity')
        Intent = autoclass('android.content.Intent')
        String = autoclass('java.lang.String')
        Uri = autoclass('android.net.Uri')
        File = autoclass('java.io.File')

        shareIntent = Intent(Intent.ACTION_SEND)
        shareIntent.setType('"image/*"')
        imageFile = File(path)
        uri = Uri.fromFile(imageFile)
        shareIntent.putExtra(Intent.EXTRA_STREAM, uri)

        currentActivity = cast('android.app.Activity', PythonActivity.mActivity)
        currentActivity.startActivity(shareIntent)

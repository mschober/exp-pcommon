import utilities
import re, os

class P4:
    #http://www.perforce.com/perforce/doc.current/manuals/p4guide/08_scripting.html
    #Common flags used in scripting and reporting: -G Causes all output (and batch input for form commands with -i) to be formatted as marshaled Python dictionary objects.
    def __init__(self, path):
        self.path = path
        self.dirs_list = []
        self.files_list = []

    def __execute_p4_command(self, cmd):
        results = [ file for file in utilities.execute_command(cmd) if not re.search(' - delete change', file) ]
        return results

    def dirs(self, sub_path=''):
        cmd = "p4 dirs %s" % ('/'.join([ path for path in [self.path, sub_path, '*'] if path ]))
        self.dirs_list = self.__execute_p4_command(cmd)
        return list(self.dirs_list)

    def files(self, sub_path='', limit=None):
        files = ('/'.join([ path for path in [self.path, sub_path, '...#head'] if path ]))
        if limit:
            cmd = "p4 files -m {max} {files}".format(max=limit, files=files)
        else:
            cmd = "p4 files {files}".format(files=files)
        self.files_list = self.__execute_p4_command(cmd)
        return list(self.files_list)

    def text(self, file_path):
        cmd = 'p4 print -q %s' % self.path + "/" + file_path
        return self.__execute_p4_command(cmd)

    def get_it(self, filename):
        cmd = 'p4 print -q %s' % os.path.join(self.path, filename)
        file_txt = self.__execute_p4_command(cmd)
        return file_txt

    def edit(self, filename):
        cmd = 'p4 edit %s' % os.path.join(self.path, filename)
        self.__execute_p4_command(cmd)

    def where(self, filename):
        cmd = 'p4 where %s' % os.path.join(self.path, filename)
        location_mapping = self.__execute_p4_command(cmd)
        local_path = location_mapping[0].split()[2]
        return local_path


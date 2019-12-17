from NBfinder import NotebookFinder
import sys
sys.meta_path.append(NotebookFinder())
from referencer import IntentReferencer

from numpy import array
from numpy import concatenate as concat

def check_exists(init):
    def init_check(label='unnamed', container=None, *args, **kwargs):
        if container:
            if label!='unnamed' and label in container['label']:
                i = container['label'].index(label)
                return container['object'][i]
            else:
                if label not in container['label']:
                    return _Intent(label+str(i), container, **kwargs)
                for i in range(200): #using this as a stop for a sanity check
                    if label+str(i) not in container['label']:
                        return _Intent(label+str(i), container, **kwargs)
                raise ValueError('Invalid intent label, too many duplicates.')
        init(label, container, *args, **kwargs)

class Intent(IntentReferencer):
    @check_exists
    def __init__(self, label='unnamed', parent=None, index=array([]), utterances=array([])):
        IntentReferencer.__init__(self)
        self.ID = id(self)
        if type(parent.state_data)!=dict:
            raise ValueError("Invalid container for intent:", str(label))
        self.parent = parent
        self.container=parent.state_data
        self.label=label
        self.index=index
        self.utterances=utterances
    
    def __str__(self):
        return "Intent: " + self.label + " | " + str(self.count) + " utterances"

    def _ipython_display_(self):
        print(self.__str__())

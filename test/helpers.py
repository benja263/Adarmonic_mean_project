import os.path
import pickle


def access_folder(folder_name='data'):
    '''
    Returns the folder path desired by putting as argument the name of the folder that is
    contained in the project folder, otherwise need to specify address.
    '''
    
    wk_dir = os.path.dirname(os.path.realpath('__file__'))
    prj_folder = os.path.abspath(os.path.join(wk_dir, os.pardir))
    
    if folder_name != 'data':
        return prj_folder + '/' + folder_name + '/'
    else:
        return prj_folder + '/' + 'data' + '/'


def save(name, object, folder_name='data'):
    path = access_folder(folder_name)
    name = path + name + '.pickle'
    with open(name, 'wb') as handle:
        pickle.dump(object, handle, protocol=pickle.HIGHEST_PROTOCOL)


def load(name, folder_name='data'):
    path = access_folder(folder_name)
    name = path + name + '.pickle'
    with open(name, 'rb') as fp:
        file = pickle.load(fp)
    return file

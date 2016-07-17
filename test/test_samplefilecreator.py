import unittest
import os
from samplefilecreator import samplefilecreator as script

#python -m unittest test.test_samplefilecreator
class TestFunctions(unittest.TestCase):
    @classmethod
    def setUpClass(self):
        self.filenames_pos = ["1.jpg", "2.jpg", "3.jpg", "8.jpg", "25.jpg"]
        self.filenames_bg = ["1.jpg", "2.jpg", "99.jpg"]
        self.filenames_jpg = ["1.jpg", "2.jpg", "3.jpg", "8.jpg", "25.jpg"]
        self.filenames_png = ["1.png", "2.png", "3.png", "8.png", "25.png"]
        self.filenames_vec = ["1.vec", "2.vec", "3.vec", "8.vec", "25.vec"]
        self.path_to_test_dir = os.getcwd() + "/ScriptTest/"
        self.path_to_bg_file = self.path_to_test_dir + "bg.txt"
        self.path_to_info_file = self.path_to_test_dir + "info.dat"
        self.path_to_pos_images = self.path_to_test_dir + "pos/"
        self.path_to_pos_resized_images = self.path_to_test_dir + "pos_resized/"
        self.path_to_one_image = self.path_to_pos_images + "1.jpg"
        self.path_to_vecs = self.path_to_test_dir + "vec/"
        self.path_to_out_vec = self.path_to_test_dir + "out.vec"

    @classmethod
    def tearDownClass(self):
        # Delete the files created in pos_resized during the test
        # we need to delete: info.dat, bg.txt, out.vec, images in vec folder and pos_resized folder
        os.remove(self.path_to_info_file)
        os.remove(self.path_to_bg_file)
        os.remove(self.path_to_out_vec)

        for filename in self.filenames_jpg:
            os.remove(self.path_to_pos_resized_images + filename)

        for filename in self.filenames_vec:
            os.remove(self.path_to_vecs + filename)

    def test_smoke(self):
        self.assertEqual(0, 0)

    def test_create_bg_file(self):
        script.create_bg_file(self.path_to_test_dir, self.filenames_bg)

        bg_string_correct = "neg/1.jpg\nneg/2.jpg\nneg/99.jpg\n"

        bg_string = ""
        with open(self.path_to_bg_file, "r") as f:
            for line in f.readlines():
                bg_string += line

        self.assertEqual(bg_string_correct, bg_string)

    def test_create_positive_file_pos(self):
        script.create_positive_file(self.path_to_test_dir, "pos/", self.filenames_pos)

        info_string_correct = "pos/1.jpg 1 0 0 50 50\npos/2.jpg 1 0 0 20 22\npos/3.jpg 1 0 0 21 21\npos/8.jpg 1 0 0 28 28\npos/25.jpg 1 0 0 44 44\n"

        info_string = ""
        with open(self.path_to_info_file, "r") as f:
            for line in f.readlines():
                info_string += line

        self.assertEqual(info_string_correct, info_string)

    def test_get_image_size(self):
        size = script.get_image_size(self.path_to_one_image)

        self.assertEqual((50,50), size)

    def test_get_all_png_files(self):
        png_files = script.get_all_png_files(self.path_to_pos_images)

        for png_filename in self.filenames_png:
            self.assertEqual(True, png_filename in png_files)

    def test_get_all_jpg_files(self):
        jpg_files = script.get_all_jpg_files(self.path_to_pos_images)

        for jpg_filename in self.filenames_jpg:
            self.assertEqual(True, jpg_filename in jpg_files)

    def test_get_mean_size(self):
        mean_size = script.get_mean_size(self.path_to_pos_images, self.filenames_jpg)

        self.assertEqual((33, 33), mean_size)

    def test_resize_images(self):
        script.resize_images(self.path_to_test_dir, self.filenames_pos, (50, 50))

        # Now we rely on the get_mean_size function we have just tested
        mean_size = script.get_mean_size(self.path_to_pos_resized_images, self.filenames_jpg)

        self.assertEqual((50,50), mean_size)

    def test_create_samples(self):
        # for now we just test if .vec files were created
        # create_samples assumes images to have the same size so we need to run this on resized images
        # for this we recreated the info.dat file to link to the resized images
        script.resize_images(self.path_to_test_dir, self.filenames_pos, (50, 50))
        script.create_positive_file(self.path_to_test_dir, "pos_resized/", self.filenames_pos)

        script.create_samples(self.filenames_pos, 10, 50, 50, 1.0, 1.0, 0.1, self.path_to_test_dir)

        for filename in self.filenames_vec:
            path_to_file = self.path_to_vecs + filename
            self.assertTrue(os.path.isfile(path_to_file))

    def test_merge_all_vecs(self):
        script.merge_all_vecs(self.path_to_test_dir, "vec/")

        self.assertTrue(os.path.isfile(self.path_to_out_vec))

if __name__ == '__main__':
    unittest.main()

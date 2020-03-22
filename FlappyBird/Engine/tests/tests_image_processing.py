import unittest

import pygame

from Engine.utils import image_processing


class LoadImagesTest(unittest.TestCase):

    @classmethod
    def setUpClass(cls) -> None:
        cls.invalid_image_path = 'invalid.inv'

        cls.single_image_path = './imgs/background.png'
        cls.multiple_image_path = './imgs/bird'

        cls.scale = (1280, 720)

    def assert_correct_scale(self, img):
        self.assertEqual(img.get_width(), self.scale[0])
        self.assertEqual(img.get_height(), self.scale[1])

    def test_should_load_valid_img(self):
        image = image_processing.load_image(self.single_image_path)

        self.assertIsNotNone(image)

    def test_should_fail_with_invalid_img(self):
        with self.assertRaises(pygame.error):
            image = image_processing.load_image(self.invalid_image_path)

    def test_should_load_valid_imgs_in_dir(self):
        images = image_processing.load_images(self.multiple_image_path)

        result = all(img is not None for img in images)
        self.assertTrue(result)

    def test_should_fail_with_invalid_imgs_dir(self):
        with self.assertRaises(FileNotFoundError):
            images = image_processing.load_images(self.invalid_image_path)

# Utils

    def test_should_scale_img(self):
        image = image_processing.load_image(self.single_image_path)
        image_scaled = image_processing.scale_image(image, self.scale)

        self.assert_correct_scale(image_scaled)

    def test_should_flip_img(self):
        image = image_processing.load_image(self.single_image_path)
        image_scaled = image_processing.flip(image, False, True)

        print('==> Test Flip <==')

# Load Utils

    def test_should_load_img_scaled(self):
        image_scaled = image_processing.load_image_scaled(self.single_image_path, self.scale)

        self.assert_correct_scale(image_scaled)

    def test_should_load_imgs_scaled(self):
        images_scaled = image_processing.load_images_scaled(self.multiple_image_path, self.scale)

        for image_scaled in images_scaled:
            self.assert_correct_scale(image_scaled)

    # def test_should_load_img_flipped(self):
    #     image_scaled = image_processing.load_image_scaled(self.single_image_path, self.scale)
    #
    #     self.assert_correct_scale(image_scaled)
    #
    # def test_should_load_imgs_flipped(self):
    #     images_scaled = image_processing.load_images_scaled(self.multiple_image_path, self.scale)
    #
    #     for image_scaled in images_scaled:
    #         self.assert_correct_scale(image_scaled)


if __name__ == '__main__':
    unittest.main()

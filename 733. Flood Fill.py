class Solution:
    # colorI = color initial, colorF = color final
    def Fill(self, image, sr, sc, colorI, colorF):
      # Check for bounds
      if ( sr < 0 or sc < 0 or sr >= len(image) or sc >= len(image[0]) ):
        return
      # Check if current pixel is the same color as the initial
      if ( image[sr][sc] == colorF or image[sr][sc] != colorI):
        return
      
      # Set pixel to colorF
      image[sr][sc] = colorF
      
      self.Fill(image, sr + 1, sc, colorI, colorF)
      self.Fill(image, sr - 1, sc, colorI, colorF)
      self.Fill(image, sr, sc + 1, colorI, colorF)
      self.Fill(image, sr, sc - 1, colorI, colorF)
      return image


    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
      self.Fill(image, sr, sc, image[sr][sc], color)
      return image
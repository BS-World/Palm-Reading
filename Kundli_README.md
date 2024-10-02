
# Bharat Kundli Application

The Bharat Kundli Application is a Python-based tool that calculates and displays astrological charts (Kundli) based on the user's birth date, time, and place. It provides planetary positions, astrological interpretations, and visual representations of the Kundli.

## Features

- **Calculate Kundli**: Calculate the positions of all major planets based on the user's birth information.
- **Geocoding**: Retrieve geographical coordinates based on the place of birth using the `geopy` library.
- **Astrological Interpretations**: Provide interpretations for each planet's position from a text file.
- **Visual Representation**: Display a bar chart of planetary positions using `matplotlib`.
- **Save Kundli**: Save the Kundli data to a text file for future reference.

## Requirements

- Python 3.x
- Required libraries:
  - `astropy`
  - `ephem`
  - `geopy`
  - `matplotlib`

## Installation

1. **Clone the repository** (or download the source code):
   ```bash
   git clone https://github.com/your_username/bharat_kundli.git
   cd bharat_kundli
   ```

2. **Install required libraries**:
   ```bash
   pip install astropy ephem geopy matplotlib
   ```

3. **Create a file named `interpretations.txt`** in the same directory as the application with the following content:
   ```
   Sun: Represents self, ego, and identity.
   Moon: Represents emotions, intuition, and subconscious.
   Mercury: Represents communication and intellect.
   Venus: Represents love, beauty, and relationships.
   Mars: Represents action, desire, and aggression.
   Jupiter: Represents growth, expansion, and good fortune.
   Saturn: Represents discipline, responsibility, and limitations.
   Uranus: Represents innovation, change, and rebellion.
   Neptune: Represents dreams, intuition, and the unconscious.
   Pluto: Represents transformation, power, and regeneration.
   ```

## Usage

1. **Run the application**:
   ```bash
   python bharat_kundli.py
   ```

2. **Input the following details** in the GUI:
   - Date of Birth (format: YYYY-MM-DD)
   - Time of Birth (format: HH:MM)
   - Place of Birth

3. **Click on "Submit"** to calculate the Kundli. The application will display:
   - A bar chart representing the planetary positions.
   - Astrological interpretations based on the planetary positions.
   - The Kundli will also be saved to a file named `kundli.txt`.

## Future Enhancements

- Implement additional astrological features and interpretations.
- Improve the user interface for better user experience.
- Enable printing options for the Kundli.

## Contributing

Contributions are welcome! Feel free to fork the repository and submit pull requests for improvements and bug fixes.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Contact

For any inquiries or issues, please contact [your_email@example.com](mailto:your_email@example.com).
```

### Customization
- **Your GitHub Username**: Replace `your_username` in the clone URL with your actual GitHub username.
- **Contact Information**: Update the email address to your own.
- **License Information**: If you are using a different license, ensure you specify that correctly.

### Additional Notes
- Make sure to test the application and verify that all features are working as intended before sharing it with others or publishing it.
- You can also add screenshots of the application in use to make the README more visually appealing.

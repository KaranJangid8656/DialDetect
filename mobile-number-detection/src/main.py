def is_valid_mobile_number(number):
    import re
    pattern = r'^\+?1?\d{10}$' 
    return re.match(pattern, number) is not None

def detect_mobile_numbers(input_data):
    mobile_numbers = []
    for line in input_data:
        words = line.split()
        for word in words:
            if is_valid_mobile_number(word):
                mobile_numbers.append(word)
    return mobile_numbers

def main():
    input_data = [
        "Contact me at +1234567890",
        "My number is 9876543210",
        "Not a number: 12345",
        "Another valid number: +19876543210",
        "Invalid number: 8431770172"
    ]
    
    detected_numbers = detect_mobile_numbers(input_data)
    print("Detected Mobile Numbers:")
    for number in detected_numbers:
        print(number)

if __name__ == "__main__":
    main()
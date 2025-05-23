{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "809e62fa-3fd2-448f-9862-26d384c00eb9",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\n",
      "Simple Command-Line Calculator\n",
      "------------------------------\n",
      "1. Addition (+)\n",
      "2. Subtraction (-)\n",
      "3. Multiplication (*)\n",
      "4. Division (/)\n",
      "5. Modulo (%)\n",
      "6. Exit\n",
      "------------------------------\n"
     ]
    },
    {
     "name": "stdin",
     "output_type": "stream",
     "text": [
      "Choose an operation (1-6):  5\n",
      "Enter the first number:  45\n",
      "Enter the second number:  69\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Result: 45.0 % 69.0 = 45.0\n",
      "\n",
      "Simple Command-Line Calculator\n",
      "------------------------------\n",
      "1. Addition (+)\n",
      "2. Subtraction (-)\n",
      "3. Multiplication (*)\n",
      "4. Division (/)\n",
      "5. Modulo (%)\n",
      "6. Exit\n",
      "------------------------------\n"
     ]
    }
   ],
   "source": [
    "def display_menu():\n",
    "    print(\"\\nSimple Command-Line Calculator\")\n",
    "    print(\"------------------------------\")\n",
    "    print(\"1. Addition (+)\")\n",
    "    print(\"2. Subtraction (-)\")\n",
    "    print(\"3. Multiplication (*)\")\n",
    "    print(\"4. Division (/)\")\n",
    "    print(\"5. Modulo (%)\")\n",
    "    print(\"6. Exit\")\n",
    "    print(\"------------------------------\")\n",
    "\n",
    "def get_number(prompt):\n",
    "    while True:\n",
    "        try:\n",
    "            return float(input(prompt))\n",
    "        except ValueError:\n",
    "            print(\"Invalid input. Please enter a numeric value.\")\n",
    "\n",
    "def perform_operation(choice):\n",
    "    num1 = get_number(\"Enter the first number: \")\n",
    "    num2 = get_number(\"Enter the second number: \")\n",
    "\n",
    "    if choice == '1':\n",
    "        result = num1 + num2\n",
    "        print(f\"Result: {num1} + {num2} = {result}\")\n",
    "    elif choice == '2':\n",
    "        result = num1 - num2\n",
    "        print(f\"Result: {num1} - {num2} = {result}\")\n",
    "    elif choice == '3':\n",
    "        result = num1 * num2\n",
    "        print(f\"Result: {num1} * {num2} = {result}\")\n",
    "    elif choice == '4':\n",
    "        if num2 == 0:\n",
    "            print(\"Error: Division by zero is not allowed.\")\n",
    "        else:\n",
    "            result = num1 / num2\n",
    "            print(f\"Result: {num1} / {num2} = {result}\")\n",
    "    elif choice == '5':\n",
    "        if num2 == 0:\n",
    "            print(\"Error: Modulo by zero is not allowed.\")\n",
    "        else:\n",
    "            result = num1 % num2\n",
    "            print(f\"Result: {num1} % {num2} = {result}\")\n",
    "    else:\n",
    "        print(\"Invalid operation.\")\n",
    "\n",
    "def main():\n",
    "    while True:\n",
    "        display_menu()\n",
    "        choice = input(\"Choose an operation (1-6): \").strip()\n",
    "        \n",
    "        if choice == '6':\n",
    "            print(\"Exiting calculator. Goodbye.\")\n",
    "            break\n",
    "        elif choice in {'1', '2', '3', '4', '5'}:\n",
    "            perform_operation(choice)\n",
    "        else:\n",
    "            print(\"Invalid choice. Please select a valid option from the menu.\")\n",
    "\n",
    "if __name__ == \"__main__\":\n",
    "    main()\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "5245e991-aafe-448d-b337-56ffe59595d3",
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3 (ipykernel)",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.12.7"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}

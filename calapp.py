import streamlit as st
import math
# Functions for scientific operations
def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y == 0:
        return "Error! Division by zero."
    else:
        return x / y

def power(x, y):
    return x ** y

def sqrt(x):
    return math.sqrt(x)

def log(x):
    if x > 0:
        return math.log(x)
    else:
        return "Error! Logarithm is only defined for positive numbers."

def sin(x):
    return math.sin(math.radians(x))

def cos(x):
    return math.cos(math.radians(x))

def tan(x):
    return math.tan(math.radians(x))

# Function to plot graphs
def plot_function(func_name):
    x = np.linspace(-360, 360, 400)  # Generate 400 points between -360 to 360 degrees
    plt.figure(figsize=(8, 5))

    if func_name == 'sin':
        y = np.sin(np.radians(x))
        plt.plot(x, y, label="sin(x)")
    elif func_name == 'cos':
        y = np.cos(np.radians(x))
        plt.plot(x, y, label="cos(x)")
    elif func_name == 'tan':
        y = np.tan(np.radians(x))
        plt.plot(x, y, label="tan(x)")
    elif func_name == 'log':
        x = np.linspace(0.1, 10, 400)  # Logarithms are only defined for positive values
        y = np.log(x)
        plt.plot(x, y, label="log(x)")
    elif func_name == 'x^2':
        y = x**2
        plt.plot(x, y, label="x^2")
    else:
        st.error("Invalid function")

    plt.title(f"Graph of {func_name}(x)")
    plt.xlabel("x-axis")
    plt.ylabel(f"{func_name}(x)")
    plt.grid(True)
    plt.legend()
    st.pyplot(plt)

# Streamlit App
st.title("🧮 Scientific Calculator with Graph Plotting")

# Input fields for numbers
operation_type = st.sidebar.selectbox(
    "Select operation",
    ("Add", "Subtract", "Multiply", "Divide", "Power (x^y)", "Square Root (√x)", "Logarithm (ln x)", "Sine (sin x)", "Cosine (cos x)", "Tangent (tan x)", "Plot Graph")
)

if operation_type in ['Add', 'Subtract', 'Multiply', 'Divide', 'Power (x^y)']:
    num1 = st.number_input("Enter first number", step=1.0, format="%.2f")
    num2 = st.number_input("Enter second number", step=1.0, format="%.2f")

    if st.button("Calculate"):
        if operation_type == "Add":
            st.success(f"The result is: {add(num1, num2)}")
        elif operation_type == "Subtract":
            st.success(f"The result is: {subtract(num1, num2)}")
        elif operation_type == "Multiply":
            st.success(f"The result is: {multiply(num1, num2)}")
        elif operation_type == "Divide":
            result = divide(num1, num2)
            if isinstance(result, str):  # Error handling
                st.error(result)
            else:
                st.success(f"The result is: {result}")
        elif operation_type == "Power (x^y)":
            st.success(f"The result is: {power(num1, num2)}")

elif operation_type == "Square Root (√x)":
    num = st.number_input("Enter a number", step=1.0, format="%.2f")
    if st.button("Calculate"):
        st.success(f"The square root of {num} is: {sqrt(num)}")

elif operation_type == "Logarithm (ln x)":
    num = st.number_input("Enter a positive number", step=1.0, format="%.2f")
    if st.button("Calculate"):
        result = log(num)
        if isinstance(result, str):
            st.error(result)
        else:
            st.success(f"The natural logarithm of {num} is: {result}")

elif operation_type in ["Sine (sin x)", "Cosine (cos x)", "Tangent (tan x)"]:
    angle = st.number_input("Enter angle in degrees", step=1.0, format="%.2f")
    if st.button("Calculate"):
        if operation_type == "Sine (sin x)":
            st.success(f"The sine of {angle}° is: {sin(angle)}")
        elif operation_type == "Cosine (cos x)":
            st.success(f"The cosine of {angle}° is: {cos(angle)}")
        elif operation_type == "Tangent (tan x)":
            st.success(f"The tangent of {angle}° is: {tan(angle)}")

elif operation_type == "Plot Graph":
    graph_choice = st.selectbox("Select graph to plot", ("sin", "cos", "tan", "log", "x^2"))
    if st.button("Plot"):
        plot_function(graph_choice)

# Footer
st.markdown("---")
st.markdown("### Designed by [Your Name](https://https://github.com/MALIK-ZAKRIA-MEHMOOD)")

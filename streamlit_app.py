import streamlit as st
import streamlit.components.v1 as components

# Your HTML code
html_code = """
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <title>Dummy Clickable Page</title>
  <style>
    body { font-family: Arial, sans-serif; padding: 20px; }
    .section { margin-bottom: 25px; }
    button, a, input, select { margin: 5px; padding: 8px 12px; }
  </style>
</head>
<body>
  <h1>Dummy Clickable Elements Page</h1>

  <div class="section">
    <h2>Buttons</h2>
    <button id="btn1">Button 1</button>
    <button id="btn2" class="primary">Button 2</button>
    <button id="btn3" disabled>Disabled Button</button>
    <input type="button" value="Input Button">
  </div>

  <div class="section">
    <h2>Links</h2>
    <a href="#home" id="link1">Go Home</a>
    <a href="#about" class="nav-link">About Us</a>
    <a href="https://example.com" target="_blank">External Link</a>
  </div>

  <div class="section">
    <h2>Form Inputs</h2>
    <label>
      Text Input: 
      <input type="text" id="username" placeholder="Enter username">
    </label>
    <br>
    <label>
      Password: 
      <input type="password" id="password">
    </label>
    <br>
    <label>
      <input type="checkbox" id="chk1"> Subscribe to newsletter
    </label>
    <label>
      <input type="checkbox" id="chk2"> Accept terms
    </label>
    <br>
    <label>
      <input type="radio" name="gender" value="male"> Male
    </label>
    <label>
      <input type="radio" name="gender" value="female"> Female
    </label>
    <br>
    <select id="dropdown">
      <option value="">-- Select option --</option>
      <option value="opt1">Option 1</option>
      <option value="opt2">Option 2</option>
      <option value="opt3">Option 3</option>
    </select>
    <br>
    <button type="submit">Submit Form</button>
  </div>

  <div class="section">
    <h2>Other Clickables</h2>
    <input type="file" id="fileUpload">
    <br>
    <input type="color" id="colorPicker">
    <br>
    <input type="date" id="datePicker">
    <br>
    <button onclick="alert('Hello!')">Button with JS</button>
  </div>

</body>
</html>
"""

# Render HTML inside Streamlit
components.html(html_code, height=800, scrolling=True)

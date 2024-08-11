import xml.etree.ElementTree as ET

vehicle_xml_data_as_string = "<motorvehicles><vehicle type='car'><registration_no>CBB1456</registration_no><make>Toyota</make><model>Premio</model></vehicle><vehicle type='van'><registration_no>PR2245</registration_no><make>Mazda</make><model>Bongo</model></vehicle></motorvehicles>"

root = ET.fromstring(vehicle_xml_data_as_string)

# Root Tag:
print(root.tag)

# Root Attributes:
print(root.attrib)

# Iterate the children nodes
for child in root:
  print(child.tag, child.attrib)
  
# Accessing by index:
root[0][1].text

# Accessing atttributes:
for attr in root[0].attrib:
  print(attr+ "=" + root[0].attrib[attr])

# Searching with Iter:
for element in root.iter(tag='registration_no'):
  print(element.text)

# Searching with findall:
for element in root.findall('vehicle'):
  regno= element.find('registration_no').text
  make= element.find('make').text
  print(regno, make)

# Modifying XML:
for element in root.iter(tag='make'):
  newmake = 'Nissan'
  element.text = newmake

# Searching after modifying:
for element in root.findall('vehicle'):
  regno= element.find('registration_no').text
  make= element.find('make').text
  print(regno, make)

# Building XML:
a = ET.Element('a')
b = ET.SubElement(a, 'b')
c = ET.SubElement(a, 'c')
d = ET.SubElement(c, 'd')
ET.dump(a)

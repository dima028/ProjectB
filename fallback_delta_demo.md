
# Billboard_AI

### Analytics Tool to Democritize Advertising for Clients & Aid Local, Toronto-based Small- and Medium-Sized Businesses in Competing against Large Businesses


```python
import ipywidgets as widgets
from IPython.display import display, Markdown
from IPython.display import HTML



#--- Calling Toggle ----
# Hide or display code button definition
HideShowCodeButton = HTML('''<script>
code_show=true; 
function code_toggle() {
 if (code_show){
 $('div.input').hide();
 } else {
 $('div.input').show();
 }
 code_show = !code_show


} 
$( document ).ready(code_toggle);
</script>
<form action="javascript:code_toggle()"><input type="submit" value="Click to toggle on/off raw code"></form>''')

# Display Hide or display code button
HideShowCodeButton
```




<script>
code_show=true; 
function code_toggle() {
 if (code_show){
 $('div.input').hide();
 } else {
 $('div.input').show();
 }
 code_show = !code_show


} 
$( document ).ready(code_toggle);
</script>
<form action="javascript:code_toggle()"><input type="submit" value="Click to toggle on/off raw code"></form>




```python
CompanyName = widgets.Text(
    description = 'Company Name:',
    style = {'description_width':'initial'}
)


Product = widgets.RadioButtons(
    options=['Travel', 'Home Appliance', 'Gaming', 'Baby Products'],
    value='Gaming',
    description='Product:',
    disabled=False
)

Price = widgets.IntSlider(
    value=700,
    min=0,
    max=1000,
    step=10,
    description='Price:',
    disabled=False,
    continuous_update=False,
    orientation='horizontal',
    readout=True,
    readout_format='d'
)

Budget = widgets.IntSlider(
    value=5000,
    min=0,
    max=30000,
    step=100,
    description='Budget:',
    disabled=False,
    continuous_update=False,
    orientation='horizontal',
    readout=True,
    readout_format='d'
)

display(Markdown('#### Please fill in the following information:'))
display(CompanyName)
display(Product)
display(Price)
display(Budget)
```


#### Please fill in the following information:



    Text(value='', description='Company Name:', style=DescriptionStyle(description_width='initial'))



    RadioButtons(description='Product:', index=2, options=('Travel', 'Home Appliance', 'Gaming', 'Baby Products'),…



    IntSlider(value=700, continuous_update=False, description='Price:', max=1000, step=10)



    IntSlider(value=5000, continuous_update=False, description='Budget:', max=30000, step=100)



```python
if Product.value == 'Gaming':
    age = 15
    youth = 10
    kid = 2
elif Product.value == 'Travel':
    age = 40
    youth = 5
    kid = 0
elif Product.value == 'Home Appliance':
    age = 55
    youth = 5
    kid = 2
elif Product.value == 'Baby Products':
    age = 30
    youth = 18
    kid = 2
    
veh = Budget.value
ped = Budget.value * 0.6

income = Price.value / 50


import pandas as pd 
import matplotlib.pyplot as plt
from sklearn.manifold import TSNE
from sklearn.cluster import KMeans

def ProjectB(veh, ped, age, income, kid, youth):
    data = pd.read_csv("Downloads\\Data-Part1.csv") 
    data = data.dropna()

    data_trunc = data.loc[:,'Vehicle Traffic':'Percent of Youth']
    #data_trunc_array=data_trunc.values
        
    #data_trunc_TSNE = TSNE(n_components=2).fit_transform(data_trunc)
        
    data_k = KMeans(n_clusters=80, random_state=0).fit(data_trunc)
    
    num = data_k.predict([[veh, ped, age, income, kid, youth]])[0]
    
    data_labels = pd.DataFrame(data_k.labels_)
    
    data_total = pd.concat([data_labels, data], axis=1)
    
    is_val = data_total[0]==num
    data_total_fin = data_total[is_val]
    return (data_total_fin['Intersection'].values[0]) 

ProjectB(veh, ped, age, income, kid, youth)
```




    'SHERBOURNE ST and RICHMOND ST E'



##### End of Workflow

import flet as ft
from flet import Row,IconButton,icons,Column,icons
import knapsacklocal as kp
from simpleai.search.viewers import BaseViewer
from simpleai.search.models import SearchProblem

from simpleai.search.local import hill_climbing,hill_climbing_random_restarts,genetic

def main(page:ft.Page):
    page.scroll="always"
    page.auto_scroll=True
    def start_search(t):
        
        num_of_items = int(number_of_items.value)
        knapsack_cap = int(knapsack_capacity.value)
        weights_of_each = list(map(int,weights_of_each_item.value.split(",")))
        values_of_each = list(map(int,values_of_each_item.value.split(",")))
        
        print(weights_of_each,"weights")
        print(values_of_each,"values")

        my_viewer = BaseViewer()
        myp = kp.KnapsackProblem(weights_of_each,values_of_each,num_of_items,knapsack_cap)
        
        #result = hill_climbing(myp,viewer=my_viewer)
        result = genetic(myp,viewer=my_viewer)
        print(result.path())
        weight=0
        value = 0 
        count=0

        for i in result.state:
            count+=1
            if i==1:
                weight += weights_of_each[count-1]


        count=0
        for i in result.state:
            count+=1
            if i==1:
                value += values_of_each[count-1]
        
        selected_items = ft.Text(value=f"Selected items: {result.state}")
        selected_weights = ft.Text(value=f"Total weight of selected items: {weight}")
        selected_values = ft.Text(value=f"Total value of selected items: {value}")
      
        selected_items = ft.Text(value=f"Selected items: {result.state}")

        page.add(selected_items,selected_weights,selected_values)
        knapsack_img = ft.Image(src="knapsack.png")
        in_knapsack = ""
        counter = 0
        for i in (result.state):
            if i == 1:
                in_knapsack += f"{counter+1}\n"
            counter+=1
        print(in_knapsack,"in knapsack")

        knap_text = ft.Container(ft.Text(value=f"{in_knapsack}",size=50,color=ft.colors.BLACK),padding=ft.padding.only(top=100,left=200))
        knapsack = ft.Stack([knapsack_img,knap_text])
        page.add(knapsack)

    number_of_items = ft.TextField(hint_text="Enter number of items",width=600,label="Enter number of items")
    knapsack_capacity = ft.TextField(hint_text="Enter knapsack capacity",width=600,label="Enter knapsack capacity")
    weights_of_each_item = ft.TextField(hint_text="Enter weights of each item (with after comma for each)",label="Enter weights of each item (with after comma for each)",width=600)
    values_of_each_item = ft.TextField(hint_text="Enter values of each item (with after comma for each)",label="Enter values of each item (with after comma for each)",width=600)
    
    start_button = ft.IconButton(icons. PLAY_CIRCLE_FILL,icon_size=50,on_click=start_search)

    
    page.add(ft.Column([number_of_items,knapsack_capacity,weights_of_each_item,values_of_each_item,start_button]))
    
    
    
    
    


if __name__ == "__main__":
    ft.app(target=main,assets_dir="assets",view=ft.WEB_BROWSER)
'''
This file is part of Giswater 2.0
The program is free software: you can redistribute it and/or modify it under the terms of the GNU 
General Public License as published by the Free Software Foundation, either version 3 of the License, 
or (at your option) any later version.
'''

# -*- coding: utf-8 -*-

from PyQt4.QtGui import QComboBox, QDateEdit, QPushButton, QTableView, QTabWidget, QLineEdit

from functools import partial

import utils_giswater
from parent_init import ParentDialog
from ui.add_sum import Add_sum          # @UnresolvedImport


def formOpen(dialog, layer, feature):
    ''' Function called when a connec is identified in the map '''
    
    global feature_dialog
    utils_giswater.setDialog(dialog)
    # Create class to manage Feature Form interaction  
    feature_dialog = ManNodeDialog(dialog, layer, feature)
    # Set button signals      
        
    #feature_dialog.dialog.findChild(QPushButton, "btn_accept").clicked.connect(feature_dialog.save)            
    #feature_dialog.dialog.findChild(QPushButton, "btn_close").clicked.connect(feature_dialog.close)
    init_config()

    
def init_config():
     
    # Manage 'connecat_id'
    nodecat_id = utils_giswater.getWidgetText("nodecat_id") 
    utils_giswater.setSelectedItem("nodecat_id", nodecat_id)   

     
class ManNodeDialog(ParentDialog):   
    
    def __init__(self, dialog, layer, feature):
        ''' Constructor class '''
        super(ManNodeDialog, self).__init__(dialog, layer, feature)      
        self.init_config_form()
        
        
    def init_config_form(self):
        ''' Custom form initial configuration '''
      
        table_element = "v_ui_element_x_node" 
        table_document = "v_ui_doc_x_node"   
        
        # Initialize variables               
        self.table_tank = self.schema_name+'."v_edit_man_tank"'
        self.table_pump = self.schema_name+'."v_edit_man_pump"'
        self.table_source = self.schema_name+'."v_edit_man_source"'
        self.table_meter = self.schema_name+'."v_edit_man_meter"'
        self.table_junction = self.schema_name+'."v_edit_man_junction"'
        self.table_manhole = self.schema_name+'."v_edit_man_manhole"'
        self.table_reduction = self.schema_name+'."v_edit_man_reduction"'
        self.table_hydrant = self.schema_name+'."v_edit_man_hydrant"'
        self.table_valve = self.schema_name+'."v_edit_man_valve"'
        self.table_waterwell = self.schema_name+'."v_edit_man_waterwell"'
              
        # Define class variables
        self.field_id = "node_id"        
        self.id = utils_giswater.getWidgetText(self.field_id, False)  
        self.filter = self.field_id+" = '"+str(self.id)+"'"                    
        self.node_type = utils_giswater.getWidgetText("node_type", False)        
        self.nodecat_id = utils_giswater.getWidgetText("nodecat_id", False) 
        
        # Get widget controls      
        self.tab_main = self.dialog.findChild(QTabWidget, "tab_main")  
        self.tbl_info = self.dialog.findChild(QTableView, "tbl_info")   
        self.tbl_document = self.dialog.findChild(QTableView, "tbl_document")  
        
        # Manage tab visibility
        self.set_tabs_visibility()  
              
        # Load data from related tables
        self.load_data()
        
        # Set layer in editing mode
        #self.layer.startEditing()
        
        # Fill the info table
        self.fill_table(self.tbl_info, self.schema_name+"."+table_element, self.filter)
        
        # Configuration of info table
        self.set_configuration(self.tbl_info, table_element)    
        
        # Fill the tab Document
        self.fill_tbl_document_man(self.tbl_document, self.schema_name+"."+table_document, self.filter)
        
        # Configuration of table Document
        self.set_configuration(self.tbl_document, table_document)
  
        # Set signals          
        self.dialog.findChild(QPushButton, "btn_doc_delete").clicked.connect(partial(self.delete_records, self.tbl_document, table_document))            
        self.dialog.findChild(QPushButton, "delete_row_info").clicked.connect(partial(self.delete_records, self.tbl_info, table_element))             
        
      
    def set_tabs_visibility(self):
        ''' Hide some tabs '''   
        
        # Get schema and table name of selected layer       
        (uri_schema, uri_table) = self.controller.get_layer_source(self.layer)   #@UnusedVariable
        if uri_table is None:
            self.controller.show_warning("Error getting table name from selected layer")
            return

        if uri_table == self.table_tank :
            for i in xrange(13,-1,-1):
                if (i != 11) & (i != 10) & (i != 0):
                    self.tab_main.removeTab(i) 
        if uri_table == self.table_pump :
            for i in xrange(13,-1,-1):
                if (i != 11) & (i != 10) & (i != 1):
                    self.tab_main.removeTab(i) 
        if uri_table == self.table_source :
            for i in xrange(13,-1,-1):
                if (i != 11) & (i != 10) & (i != 2):
                    self.tab_main.removeTab(i) 
        if uri_table == self.table_meter :
            for i in xrange(13,-1,-1):
                if (i != 11) & (i != 10) & (i != 3):
                    self.tab_main.removeTab(i) 
        if uri_table == self.table_junction :
            for i in xrange(13,-1,-1):
                if (i != 11) & (i != 10) & (i != 4):
                    self.tab_main.removeTab(i) 
        if uri_table == self.table_waterwell :
            for i in xrange(13,-1,-1):
                if (i != 11) & (i != 10) & (i != 5):
                    self.tab_main.removeTab(i) 
                    
        if uri_table == self.table_reduction :
            for i in xrange(13,-1,-1):
                if (i != 11) & (i != 10) & (i != 6):
                    self.tab_main.removeTab(i) 
        if uri_table == self.table_hydrant :
            for i in xrange(13,-1,-1):
                if (i != 11) & (i != 10) & (i != 7):
                    self.tab_main.removeTab(i) 
        if uri_table == self.table_valve :
            for i in xrange(13,-1,-1):
                if (i != 11) & (i != 10) & (i != 8):
                    self.tab_main.removeTab(i) 
        if uri_table == self.table_manhole :
            for i in xrange(13,-1,-1):
                if (i != 11) & (i != 10) & (i != 5):
                    self.tab_main.removeTab(i) 
                    
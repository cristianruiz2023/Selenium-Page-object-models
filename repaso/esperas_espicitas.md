# Condiciones Predefinidas en Selenium
## Función	                   Descripción
`alert_is_present()`	Espera a que aparezca un alert y cambia al mismo.
`all_of(*expected_conditions)`	Espera a que todas las condiciones especificadas sean verdaderas (AND lógico).
`any_of(*expected_conditions)`	Espera a que al menos una de las condiciones especificadas sea verdadera (OR lógico).
`element_attribute_to_include(locator, attribute)`	Espera a que el atributo dado esté incluido en el elemento especificado.
`element_located_selection_state_to_be(locator, is_selected)`	Espera a que el estado de selección del elemento especificado coincida con el estado proporcionado.
`element_located_to_be_selected(locator)`	Espera a que el elemento especificado esté seleccionado.
`element_selection_state_to_be(element, is_selected)`	Espera a que el estado de selección del elemento dado coincida con el estado proporcionado.
`element_to_be_clickable(mark)`	Espera a que un elemento sea visible y habilitado para hacer clic.
`element_to_be_selected(element)`	Espera a que la selección del elemento especificado esté seleccionada.
`frame_to_be_available_and_switch_to_it(locator)`	Espera a que el marco especificado esté disponible para cambiar a él.
`invisibility_of_element(element)`	Espera a que un elemento no sea visible o no esté presente en el DOM.
`invisibility_of_element_located(locator)`	Espera a que un elemento especificado no sea visible o no esté presente en el DOM.
`new_window_is_opened(current_handles)`	Espera a que se abra una nueva ventana y que el número de identificadores de ventanas aumente.
`none_of(*expected_conditions)`	Espera a que ninguna de las condiciones especificadas sea verdadera (NOT-OR lógico).
`number_of_windows_to_be(num_windows)`	Espera a que el número de ventanas sea igual a un valor determinado.
`presence_of_all_elements_located(locator)`	Espera a que haya al menos un elemento presente en la página web.
`presence_of_element_located(locator)`	Espera a que un elemento esté presente en el DOM de una página.
`staleness_of(element)`	Espera a que un elemento ya no esté adjunto al DOM.
`text_to_be_present_in_element(locator, text)`	Espera a que el texto dado esté presente en el elemento especificado.
`text_to_be_present_in_element_attribute(locator, attribute, text)`	Espera a que el texto dado esté presente en el atributo del elemento especificado.
`text_to_be_present_in_element_value(locator, text)`	Espera a que el texto dado esté presente en el valor del elemento especificado.
`title_contains(title)`	Espera a que el título contenga una subcadena (sensible a mayúsculas y minúsculas).
`title_is(title)`	Espera a que el título de la página sea exactamente igual al título esperado.
`url_changes(url)`	Espera a que la URL actual sea diferente de la URL esperada.
`url_contains(url)`	Espera a que la URL actual contenga una subcadena (sensible a mayúsculas y minúsculas).
`url_matches(pattern)`	Espera a que la URL actual coincida con un patrón proporcionado.
`url_to_be(url)`	Espera a que la URL actual sea exactamente igual a la URL esperada.
`visibility_of(element)`	Espera a que un elemento, conocido por estar presente en el DOM, sea visible.
`visibility_of_all_elements_located(locator)`	Espera a que todos los elementos estén presentes en el DOM y sean visibles.
`visibility_of_any_elements_located(locator)`	Espera a que haya al menos un elemento visible en una página web.
`visibility_of_element_located(locator)`	Espera a que un elemento esté presente en el DOM y sea visible.

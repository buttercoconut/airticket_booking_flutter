import 'package:flutter/material.dart';

class FlightSearchForm extends StatefulWidget {
  final void Function(String origin, String destination, DateTime date) onSearch;

  FlightSearchForm({required this.onSearch});

  @override
  _FlightSearchFormState createState() => _FlightSearchFormState();
}

class _FlightSearchFormState extends State<FlightSearchForm> {
  final _originController = TextEditingController();
  final _destinationController = TextEditingController();
  DateTime? _selectedDate;

  @override
  Widget build(BuildContext context) {
    return Padding(
      padding: const EdgeInsets.all(8.0),
      child: Column(
        children: [
          TextField(
            controller: _originController,
            decoration: InputDecoration(labelText: 'Origin'),
          ),
          TextField(
            controller: _destinationController,
            decoration: InputDecoration(labelText: 'Destination'),
          ),
          Row(
            children: [
              Expanded(
                child: Text(_selectedDate == null
                    ? 'Select Date'
                    : _selectedDate!.toLocal().toString().split(' ')[0]),
              ),
              TextButton(
                onPressed: () async {
                  final picked = await showDatePicker(
                    context: context,
                    initialDate: DateTime.now(),
                    firstDate: DateTime.now(),
                    lastDate: DateTime.now().add(Duration(days: 365)),
                  );
                  if (picked != null) {
                    setState(() {
                      _selectedDate = picked;
                    });
                  }
                },
                child: Text('Pick Date'),
              ),
            ],
          ),
          ElevatedButton(
            onPressed: () {
              if (_originController.text.isNotEmpty &&
                  _destinationController.text.isNotEmpty &&
                  _selectedDate != null) {
                widget.onSearch(
                  _originController.text,
                  _destinationController.text,
                  _selectedDate!,
                );
              }
            },
            child: Text('Search'),
          ),
        ],
      ),
    );
  }
}

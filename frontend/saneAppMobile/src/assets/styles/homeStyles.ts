// src/assets/styles/homeStyles.ts
import { StyleSheet } from 'react-native';

const styles = StyleSheet.create({
  container: {
    flex: 1,
    backgroundColor: '#fff',
  },
  toolbar: {
    flexDirection: 'row',
    alignItems: 'center',
    justifyContent: 'space-between',
    paddingHorizontal: 16,
    paddingTop: 40,
    paddingBottom: 10,
    backgroundColor: 'transparent',
  },
  userIcon: {
    width: 30,
    height: 30,
    borderRadius: 15,
  },
  menu: {
    flexDirection: 'row',
    gap: 20,
  },
  menuItemWrapper: {
    alignItems: 'center',
  },
  menuItem: {
    fontSize: 16,
    color: 'black',
    fontWeight: '500',
  },
  menuItemSelected: {
    fontWeight: 'bold',
  },
  underline: {
    marginTop: 2,
    height: 2,
    width: '100%',
    backgroundColor: 'orange',
  },
  content: {
    flex: 1,
    padding: 20,
  },
  uploadContainer: {
  marginTop: 40,
  alignItems: 'center',
  justifyContent: 'center',
},
uploadTitle: {
  fontSize: 18,
  fontWeight: 'bold',
  color: '#000',
  marginBottom: 20,
},
uploadButton: {
  backgroundColor: '#ff5900', // laranja
  paddingVertical: 10,
  paddingHorizontal: 20,
  borderRadius: 8,
  elevation: 2,
},
uploadButtonText: {
  color: '#fff',
  fontSize: 16,
  fontWeight: 'bold',
},
});

export default styles;
